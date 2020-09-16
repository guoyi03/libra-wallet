# flake8: noqa
from __future__ import annotations
from libra.ledger_info import LedgerInfo, LedgerInfoWithSignatures
from libra.epoch_info import EpochInfo
from libra.validator_verifier import VerifyError, ValidatorVerifier
from libra.epoch_change import EpochChangeProof, VerifierType
from libra.hasher import *
from libra.proof.transaction_with_proof import TransactionWithProof
from libra.proof.transaction_list_with_proof import TransactionListWithProof
from libra.proof.account_state_with_proof import AccountStateWithProof
from libra.proof.event_with_proof import EventWithProof
from libra.transaction import SignedTransaction, TransactionInfo
from libra.account_address import Address
from libra.access_path import AccessPath
from libra.rustlib import ensure, bail
from libra.account_resource import AccountResource
from canoser import Uint64
from typing import List, Optional
from dataclasses import dataclass
import libra.proto.get_with_proof_pb2 as get_with_proof_pb2
from libra.proto_helper import ProtoHelper


@dataclass
class UpdateToLatestLedgerRequest:
    # TODO: defined here, but not used in client. client directly use the proto's type.
    client_known_version: Uint64
    requested_items: List[RequestItem]

    @classmethod
    def from_proto(cls, proto):
        requested_items = [RequestItem.from_proto(x) for x in proto.requested_items]
        return cls(proto.client_known_version, requested_items)


@dataclass
class UpdateToLatestLedgerResponse:
    response_items: List[ResponseItem]
    ledger_info_with_sigs: LedgerInfoWithSignatures
    epoch_change_proof: EpochChangeProof
    ledger_consistency_proof: AccumulatorConsistencyProof

    def to_proto(self):
        ret = get_with_proof_pb2.UpdateToLatestLedgerResponse()
        for x in self.response_items:
            item = ret.response_items.add()
            x.to_proto_oneof(item)
        ret.ledger_info_with_sigs.MergeFrom(ProtoHelper.to_proto(self.ledger_info_with_sigs))
        ret.epoch_change_proof.MergeFrom(ProtoHelper.to_proto(self.epoch_change_proof))
        ret.ledger_consistency_proof.MergeFrom(ProtoHelper.to_proto(self.ledger_consistency_proof))
        return ret


class RequestItem:
    @classmethod
    def from_proto(cls, req_item):
        x = req_item.WhichOneof('requested_items')
        if x == 'get_account_transaction_by_sequence_number_request':
            item = req_item.get_account_transaction_by_sequence_number_request
            return GetAccountTransactionBySequenceNumberRequest.from_proto(item)
        elif x == 'get_account_state_request':
            item = req_item.get_account_state_request
            return GetAccountStateRequest.from_proto(item)
        elif x == 'get_events_by_event_access_path_request':
            item = req_item.get_events_by_event_access_path_request
            return GetEventsByEventAccessPathRequest.from_proto(item)
        elif x == 'get_transactions_request':
            item = req_item.get_transactions_request
            return GetTransactionsRequest.from_proto(item)
        else:
            bail(f"Unknown request item: {x}")


@dataclass
class GetAccountTransactionBySequenceNumberRequest(RequestItem):
    account: Address
    sequence_number: Uint64
    fetch_events: bool

    @classmethod
    def from_proto(cls, req_item):
        return cls(req_item.account, req_item.sequence_number, req_item.fetch_events)


@dataclass
class GetAccountStateRequest(RequestItem):
    address: Address

    @classmethod
    def from_proto(cls, req_item):
        return cls(req_item.address)


@dataclass
class GetEventsByEventAccessPathRequest(RequestItem):
    access_path: AccessPath
    start_event_seq_num: Uint64
    ascending: bool
    limit: Uint64

    @classmethod
    def from_proto(cls, req_item):
        return cls(
            req_item.access_path,
            req_item.start_event_seq_num,
            req_item.ascending,
            req_item.limit
        )


@dataclass
class GetTransactionsRequest(RequestItem):
    start_version: Version
    limit: Uint64
    fetch_events: bool

    @classmethod
    def from_proto(cls, req_item):
        return cls(
            req_item.start_version,
            req_item.limit,
            req_item.fetch_events
        )


class ResponseItem:
    pass


@dataclass
class GetAccountTransactionBySequenceNumberResponse(ResponseItem):
    transaction_with_proof: Optional[TransactionWithProof]
    proof_of_current_sequence_number: Optional[AccountStateWithProof]

    def to_proto_oneof(self, proto_item: ResponseItem) -> None:
        proto_item.get_account_transaction_by_sequence_number_response\
            .MergeFrom(ProtoHelper.to_proto(self))


@dataclass
class GetAccountStateResponse(ResponseItem):
    account_state_with_proof: AccountStateWithProof

    def to_proto_oneof(self, proto_item: ResponseItem) -> None:
        proto_item.get_account_state_response\
            .MergeFrom(ProtoHelper.to_proto(self))


@dataclass
class GetEventsByEventAccessPathResponse(ResponseItem):
    events_with_proof: List[EventWithProof]
    proof_of_latest_event: AccountStateWithProof
    # TODO: Rename this field to proof_of_event_handle.

    def to_proto_oneof(self, proto_item: ResponseItem) -> None:
        proto_item.get_events_by_event_access_path_response\
            .MergeFrom(ProtoHelper.to_proto(self))


@dataclass
class GetTransactionsResponse(ResponseItem):
    txn_list_with_proof: TransactionListWithProof

    def to_proto_oneof(self, proto_item: ResponseItem) -> None:
        proto_item.get_transactions_response\
            .MergeFrom(ProtoHelper.to_proto(self))


def verify(verifier_type, request, response) -> Optional[EpochInfo]:
    return verify_update_to_latest_ledger_response(
        verifier_type,
        request.client_known_version,
        request.requested_items,
        response.response_items,
        LedgerInfoWithSignatures.from_proto(response.ledger_info_with_sigs),
        EpochChangeProof.from_proto(response.epoch_change_proof),
    )


def verify_update_to_latest_ledger_response(
    verifier_type,
    req_client_known_version,
    requested_items,
    response_items,
    ledger_info_with_sigs,
    epoch_change_proof
) -> Optional[EpochInfo]:
    ledger_info = ledger_info_with_sigs.ledger_info
    signatures = ledger_info_with_sigs.signatures
    if ledger_info.version < req_client_known_version:
        raise VerifyError(f"ledger_info.version:{ledger_info.version} < {req_client_known_version}.")
    # if ledger_info.version > 0 or signatures.__len__() > 0:
    #     validator_verifier.batch_verify_aggregated_signature(ledger_info.hash(), signatures)
    if len(response_items) != len(requested_items):
        raise VerifyError(f"{len(response_items)} != {len(requested_items)}")

    for req_item, resp_item in zip(requested_items, response_items):
        verify_response_item(ledger_info, req_item, resp_item)

    if verifier_type.epoch_change_verification_required(ledger_info.epoch):
        epoch_change_li = epoch_change_proof.verify(verifier_type)
        if not epoch_change_li.ledger_info.has_next_epoch_info():
            raise VerifyError("No ValidatorSet in EpochProof")

        new_epoch_info = epoch_change_li.ledger_info.next_epoch_info.value
        new_verifier = VerifierType('TrustedVerifier', new_epoch_info)
        new_verifier.verify(ledger_info_with_sigs)
        return new_epoch_info
    else:
        verifier_type.verify(ledger_info_with_sigs)
        return None


def verify_response_item(ledger_info, requested_item, response_item):
    req_type = requested_item.WhichOneof('requested_items')
    if not req_type.endswith("_request"):
        raise VerifyError(f"RequestItem type unknown{req_type}.")
    resp_type = req_type.replace("_request", "_response")
    resp_type2 = response_item.WhichOneof('response_items')
    if resp_type != resp_type2:
        raise VerifyError(f"RequestItem/ResponseItem types mismatch:{resp_type} - {resp_type2}.")
    if resp_type == "get_account_state_response":
        asp = response_item.get_account_state_response.account_state_with_proof
        AccountStateWithProof.from_proto(asp).verify(ledger_info, ledger_info.version,
                                                     requested_item.get_account_state_request.address)
    elif resp_type == "get_account_transaction_by_sequence_number_response":
        atreq = requested_item.get_account_transaction_by_sequence_number_request
        atresp = response_item.get_account_transaction_by_sequence_number_response
        verify_get_txn_by_seq_num_resp(
            ledger_info,
            atreq.account,
            atreq.sequence_number,
            atreq.fetch_events,
            atresp.transaction_with_proof,
            atresp.proof_of_current_sequence_number
        )
    elif resp_type == "get_events_by_event_access_path_response":
        ereq = requested_item.get_events_by_event_access_path_request
        eresp = response_item.get_events_by_event_access_path_response

        verify_get_events_by_access_path_resp(
            ledger_info,
            ereq.access_path,
            ereq.start_event_seq_num,
            ereq.ascending,
            ereq.limit,
            [EventWithProof.from_proto(x) for x in eresp.events_with_proof],
            AccountStateWithProof.from_proto(eresp.proof_of_latest_event)
        )
    elif resp_type == "get_transactions_response":
        req = requested_item.get_transactions_request
        start_version = req.start_version
        limit = req.limit
        fetch_events = req.fetch_events
        txp = response_item.get_transactions_response.txn_list_with_proof
        verify_get_txns_resp(ledger_info, start_version, limit, fetch_events, txp)
    else:
        raise VerifyError(f"unknown response type:{resp_type}")


def verify_get_txn_by_seq_num_resp(
    ledger_info,
    account,
    sequence_number,
    fetch_events,
    transaction_with_proof,
    proof_of_current_sequence_number
):
    has_stx = len(transaction_with_proof.__str__()) > 0
    has_cur = len(proof_of_current_sequence_number.__str__()) > 0
    if has_stx and not has_cur:
        ensure(
            fetch_events == transaction_with_proof.HasField("events"),
            "Bad GetAccountTxnBySeqNum response. Events requested: {}, events returned: {}.",
            fetch_events,
            transaction_with_proof.HasField("events")
        )
        TransactionWithProof.from_proto(transaction_with_proof).verify_user_txn(
            ledger_info,
            transaction_with_proof.version,
            account,
            sequence_number
        )
    elif has_cur and not has_stx:
        sequence_number_in_ledger = AccountResource.get_account_resource_or_default(
            proof_of_current_sequence_number.blob).sequence_number
        ensure(
            sequence_number_in_ledger <= sequence_number,
            "Server returned no transactions while it should. Seq num requested: {}, latest seq num in ledger: {}.",
            sequence_number,
            sequence_number_in_ledger
        )
        AccountStateWithProof.from_proto(proof_of_current_sequence_number).verify(ledger_info,
                                                                                  ledger_info.version, account)
    else:
        bail(
            "Bad GetAccountTxnBySeqNum response. txn_proof.is_none():{}, cur_seq_num_proof.is_none():{}",
            has_stx,
            has_cur
        )


def verify_get_events_by_access_path_resp(
    ledger_info: LedgerInfo,
    req_access_path: AccessPath,
    req_start_seq_num: Uint64,
    req_ascending: bool,
    req_limit: Uint64,
    events_with_proof: List[EventWithProof],
    proof_of_latest_event: AccountStateWithProof
):
    proof_of_latest_event.verify(ledger_info, ledger_info.version, req_access_path.address)
    (expected_event_key_opt, seq_num_upper_bound) =\
            proof_of_latest_event.get_event_key_and_count_by_query_path(req_access_path.path)
    expected_seq_nums = gen_events_resp_idxs(seq_num_upper_bound,
                                             req_start_seq_num, req_ascending, req_limit)
    ensure(
        len(expected_seq_nums) == len(events_with_proof),
        "Expecting {} events, got {}.",
        len(expected_seq_nums),
        len(events_with_proof)
    )
    if expected_event_key_opt is not None:
        zipped = zip(events_with_proof, expected_seq_nums)
        for event_with_proof, seq_num in zipped:
            event_with_proof.verify(
                ledger_info,
                expected_event_key_opt,
                seq_num,
                event_with_proof.transaction_version,
                event_with_proof.event_index
            )
    elif events_with_proof:
        bail("Bad events_with_proof: nonempty event list for nonexistent account")


def gen_events_resp_idxs(seq_num_upper_bound, req_start_seq_num, req_ascending, req_limit):
    if not req_ascending and req_start_seq_num == Uint64.max_value and seq_num_upper_bound > 0:
        cursor = seq_num_upper_bound - 1
    else:
        cursor = req_start_seq_num
    if cursor >= seq_num_upper_bound:
        return []  # Unreachable, so empty.
    elif req_ascending:
        # Ascending, from start to upper bound or limit.
        realupper = min(cursor + req_limit, seq_num_upper_bound)
        return [x for x in range(cursor, realupper)]
    elif cursor + 1 < req_limit:
        return [x for x in range(cursor, -1, -1)]  # Descending and hitting 0.
    else:
        bottom = cursor + 1 - req_limit
        return [x for x in range(cursor, bottom - 1, -1)]  # Descending and hitting limit.


def verify_get_txns_resp(ledger_info, start_version, limit, fetch_events, txn_list_with_proof):
    if limit == 0 or start_version > ledger_info.version:
        TransactionListWithProof.from_proto(txn_list_with_proof).verify(ledger_info, None)
        return
    if fetch_events != txn_list_with_proof.HasField("events_for_versions"):
        raise VerifyError(f"fetch_events: {fetch_events} mismatch with events_for_versions")
    num_txns = len(txn_list_with_proof.transactions)
    ret_num = min(limit, ledger_info.version - start_version + 1)
    if num_txns != ret_num:
        raise VerifyError(f"transaction number expected:{ret_num}, returned:{num_txns}.")
    TransactionListWithProof.from_proto(txn_list_with_proof).verify(ledger_info, start_version)
