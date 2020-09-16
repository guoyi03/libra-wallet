bytecodes = {
  'add_currency_to_account' : b'\xa1\x1c\xeb\x0b\x01\x00\x00\x00\x06\x01\x00\x02\x03\x02\x06\x04\x08\x02\x05\n\x07\x07\x11\x1a\x08+\x10\x00\x00\x00\x01\x00\x01\x01\x01\x00\x02\x01\x06\x0c\x00\x01\t\x00\x0cLibraAccount\x0cadd_currency\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x01\x01\x01\x00\x01\x03\x0b\x008\x00\x02',
  'add_recovery_rotation_capability' : b'\xa1\x1c\xeb\x0b\x01\x00\x00\x00\x06\x01\x00\x04\x02\x04\x04\x03\x08\n\x05\x12\x0f\x07!k\x08\x8c\x01\x10\x00\x00\x00\x01\x00\x02\x01\x00\x00\x03\x00\x01\x00\x01\x04\x02\x03\x00\x01\x06\x0c\x01\x08\x00\x02\x08\x00\x05\x00\x02\x06\x0c\x05\x0cLibraAccount\x0fRecoveryAddress\x15KeyRotationCapability\x1fextract_key_rotation_capability\x17add_rotation_capability\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x01\x00\x04\x03\x05\x0b\x00\x11\x00\n\x01\x11\x01\x02',
  'add_validator_and_reconfigure' : b"\xa1\x1c\xeb\x0b\x01\x00\x00\x00\x05\x01\x00\x06\x03\x06\x0f\x05\x15\x18\x07-\\\x08\x89\x01\x10\x00\x00\x00\x01\x00\x02\x01\x03\x00\x01\x00\x02\x04\x02\x03\x00\x00\x05\x04\x01\x00\x02\x06\x0c\x03\x00\x01\x05\x01\n\x02\x02\x06\x0c\x05\x04\x06\x0c\x03\n\x02\x05\x02\x01\x03\x0bLibraSystem\x0cSlidingNonce\x0fValidatorConfig\x15record_nonce_or_abort\x0eget_human_name\radd_validator\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x01\x00\x05\x06\x12\n\x00\n\x01\x11\x00\n\x03\x11\x01\x0b\x02!\x0c\x04\x0b\x04\x03\x0e\x0b\x00\x01\x06\x00\x00\x00\x00\x00\x00\x00\x00'\x0b\x00\n\x03\x11\x02\x02",
  'burn' : b'\xa1\x1c\xeb\x0b\x01\x00\x00\x00\x06\x01\x00\x04\x03\x04\x0b\x04\x0f\x02\x05\x11\x11\x07".\x08P\x10\x00\x00\x00\x01\x01\x02\x00\x01\x00\x00\x03\x02\x01\x01\x01\x01\x04\x02\x06\x0c\x03\x00\x02\x06\x0c\x05\x03\x06\x0c\x03\x05\x01\t\x00\x05Libra\x0cSlidingNonce\x15record_nonce_or_abort\x04burn\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x01\x01\x01\x03\x01\x07\n\x00\n\x01\x11\x00\x0b\x00\n\x028\x00\x02',
  'burn_txn_fees' : b'\xa1\x1c\xeb\x0b\x01\x00\x00\x00\x06\x01\x00\x02\x03\x02\x06\x04\x08\x02\x05\n\x07\x07\x11\x19\x08*\x10\x00\x00\x00\x01\x00\x01\x01\x01\x00\x02\x01\x06\x0c\x00\x01\t\x00\x0eTransactionFee\tburn_fees\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x01\x01\x01\x00\x01\x03\x0b\x008\x00\x02',
  'cancel_burn' : b'\xa1\x1c\xeb\x0b\x01\x00\x00\x00\x06\x01\x00\x02\x03\x02\x06\x04\x08\x02\x05\n\x08\x07\x12\x19\x08+\x10\x00\x00\x00\x01\x00\x01\x01\x01\x00\x02\x02\x06\x0c\x05\x00\x01\t\x00\x0cLibraAccount\x0bcancel_burn\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x01\x01\x01\x00\x01\x04\x0b\x00\n\x018\x00\x02',
  'create_child_vasp_account' : b'\xa1\x1c\xeb\x0b\x01\x00\x00\x00\x08\x01\x00\x02\x02\x02\x04\x03\x06\x16\x04\x1c\x04\x05 #\x07C{\x08\xbe\x01\x10\x06\xce\x01\x04\x00\x00\x00\x01\x01\x00\x00\x02\x00\x01\x01\x01\x00\x03\x02\x03\x00\x00\x04\x04\x01\x01\x01\x00\x05\x03\x01\x00\x00\x06\x02\x06\x04\x06\x0c\x05\n\x02\x01\x00\x01\x06\x0c\x01\x08\x00\x05\x06\x08\x00\x05\x03\n\x02\n\x02\x05\x06\x0c\x05\n\x02\x01\x03\x01\t\x00\x0cLibraAccount\x12WithdrawCapability\x19create_child_vasp_account\x1bextract_withdraw_capability\x08pay_from\x1brestore_withdraw_capability\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x01\n\x02\x01\x00\x01\x01\x05\x03\x19\n\x00\n\x01\x0b\x02\n\x038\x00\n\x04\x06\x00\x00\x00\x00\x00\x00\x00\x00$\x03\n\x05\x16\x0b\x00\x11\x01\x0c\x05\x0e\x05\n\x01\n\x04\x07\x00\x07\x008\x01\x0b\x05\x11\x03\x05\x18\x0b\x00\x01\x02',
  'create_designated_dealer' : b'\xa1\x1c\xeb\x0b\x01\x00\x00\x00\x06\x01\x00\x04\x03\x04\x0b\x04\x0f\x02\x05\x11#\x074I\x08}\x10\x00\x00\x00\x01\x01\x02\x00\x01\x00\x00\x03\x02\x01\x01\x01\x01\x04\x02\x06\x0c\x03\x00\x07\x06\x0c\x05\n\x02\n\x02\n\x02\n\x02\x01\x08\x06\x0c\x03\x05\n\x02\n\x02\n\x02\n\x02\x01\x01\t\x00\x0cLibraAccount\x0cSlidingNonce\x15record_nonce_or_abort\x18create_designated_dealer\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x01\x01\x01\x03\x01\x0c\n\x00\n\x01\x11\x00\x0b\x00\n\x02\x0b\x03\x0b\x04\x0b\x05\x0b\x06\n\x078\x00\x02',
  'create_parent_vasp_account' : b'\xa1\x1c\xeb\x0b\x01\x00\x00\x00\x06\x01\x00\x04\x03\x04\x0b\x04\x0f\x02\x05\x11#\x074K\x08\x7f\x10\x00\x00\x00\x01\x01\x02\x00\x01\x00\x00\x03\x02\x01\x01\x01\x01\x04\x02\x06\x0c\x03\x00\x07\x06\x0c\x05\n\x02\n\x02\n\x02\n\x02\x01\x08\x06\x0c\x03\x05\n\x02\n\x02\n\x02\n\x02\x01\x01\t\x00\x0cLibraAccount\x0cSlidingNonce\x15record_nonce_or_abort\x1acreate_parent_vasp_account\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x01\x01\x01\x03\x01\x0c\n\x00\n\x01\x11\x00\x0b\x00\n\x02\x0b\x03\x0b\x04\x0b\x05\x0b\x06\n\x078\x00\x02',
  'create_recovery_address' : b'\xa1\x1c\xeb\x0b\x01\x00\x00\x00\x06\x01\x00\x04\x02\x04\x04\x03\x08\n\x05\x12\x0c\x07\x1e[\x08y\x10\x00\x00\x00\x01\x00\x02\x01\x00\x00\x03\x00\x01\x00\x01\x04\x02\x03\x00\x01\x06\x0c\x01\x08\x00\x02\x06\x0c\x08\x00\x00\x0cLibraAccount\x0fRecoveryAddress\x15KeyRotationCapability\x1fextract_key_rotation_capability\x07publish\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x01\x00\x00\x03\x05\n\x00\x0b\x00\x11\x00\x11\x01\x02',
  'create_testing_account' : b'\xa1\x1c\xeb\x0b\x01\x00\x00\x00\x07\x01\x00\x02\x03\x02\x06\x04\x08\x02\x05\n\x18\x07"(\x08J\x10\x06ZD\x00\x00\x00\x01\x00\x01\x01\x01\x00\x03\x07\x06\x0c\x05\n\x02\n\x02\n\x02\n\x02\x01\x00\x04\x06\x0c\x05\n\x02\x01\x01\t\x00\x0cLibraAccount\x1acreate_parent_vasp_account\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x01\n\x02\x08\x07testnet\n\x02\x12\x11https://libra.org\n\x02! \xb7\xa3\xc1-\xc0\xc8\xc7H\xab\x07R[p\x11"\xb8\x8b\xd7\x8f`\x0cv4-\'\xf2^_\x92DL\xde\x01\x01\x02\x01\t\x0b\x00\n\x01\x0b\x02\x07\x00\x07\x01\x07\x02\n\x038\x00\x02',
  'create_validator_account' : b'\xa1\x1c\xeb\x0b\x01\x00\x00\x00\x05\x01\x00\x04\x03\x04\n\x05\x0e\x16\x07$I\x08m\x10\x00\x00\x00\x01\x01\x02\x00\x01\x00\x00\x03\x02\x01\x00\x02\x06\x0c\x03\x00\x04\x06\x0c\x05\n\x02\n\x02\x05\x06\x0c\x03\x05\n\x02\n\x02\x0cLibraAccount\x0cSlidingNonce\x15record_nonce_or_abort\x18create_validator_account\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x01\x00\x03\x01\t\n\x00\n\x01\x11\x00\x0b\x00\n\x02\x0b\x03\x0b\x04\x11\x01\x02',
  'create_validator_operator_account' : b'\xa1\x1c\xeb\x0b\x01\x00\x00\x00\x05\x01\x00\x04\x03\x04\n\x05\x0e\x16\x07$R\x08v\x10\x00\x00\x00\x01\x01\x02\x00\x01\x00\x00\x03\x02\x01\x00\x02\x06\x0c\x03\x00\x04\x06\x0c\x05\n\x02\n\x02\x05\x06\x0c\x03\x05\n\x02\n\x02\x0cLibraAccount\x0cSlidingNonce\x15record_nonce_or_abort!create_validator_operator_account\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x01\x00\x03\x01\t\n\x00\n\x01\x11\x00\x0b\x00\n\x02\x0b\x03\x0b\x04\x11\x01\x02',
  'freeze_account' : b'\xa1\x1c\xeb\x0b\x01\x00\x00\x00\x05\x01\x00\x04\x03\x04\n\x05\x0e\x0e\x07\x1cB\x08^\x10\x00\x00\x00\x01\x00\x02\x00\x01\x00\x01\x03\x02\x01\x00\x02\x06\x0c\x05\x00\x02\x06\x0c\x03\x03\x06\x0c\x03\x05\x0fAccountFreezing\x0cSlidingNonce\x0efreeze_account\x15record_nonce_or_abort\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x01\x00\x03\x01\x07\n\x00\n\x01\x11\x01\x0b\x00\n\x02\x11\x00\x02',
  'mint_lbr' : b'\xa1\x1c\xeb\x0b\x01\x00\x00\x00\x06\x01\x00\x02\x02\x02\x04\x03\x06\x0f\x05\x15\x10\x07%c\x08\x88\x01\x10\x00\x00\x00\x01\x01\x00\x00\x02\x00\x01\x00\x00\x03\x01\x02\x00\x00\x04\x03\x02\x00\x01\x06\x0c\x01\x08\x00\x00\x02\x06\x08\x00\x03\x02\x06\x0c\x03\x0cLibraAccount\x12WithdrawCapability\x1bextract_withdraw_capability\x1brestore_withdraw_capability\nstaple_lbr\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x01\x00\x04\x01\t\x0b\x00\x11\x00\x0c\x02\x0e\x02\n\x01\x11\x02\x0b\x02\x11\x01\x02',
  'modify_publishing_option' : b'\xa1\x1c\xeb\x0b\x01\x00\x00\x00\x05\x01\x00\x02\x03\x02\x05\x05\x07\x06\x07\r$\x081\x10\x00\x00\x00\x01\x00\x01\x00\x02\x06\x0c\n\x02\x00\rLibraVMConfig\x15set_publishing_option\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x01\x00\x00\x01\x04\x0b\x00\x0b\x01\x11\x00\x02',
  'peer_to_peer_with_metadata' : b'\xa1\x1c\xeb\x0b\x01\x00\x00\x00\x07\x01\x00\x02\x02\x02\x04\x03\x06\x10\x04\x16\x02\x05\x18\x1d\x075a\x08\x96\x01\x10\x00\x00\x00\x01\x01\x00\x00\x02\x00\x01\x00\x00\x03\x02\x03\x01\x01\x00\x04\x01\x03\x00\x01\x05\x01\x06\x0c\x01\x08\x00\x05\x06\x08\x00\x05\x03\n\x02\n\x02\x00\x05\x06\x0c\x05\x03\n\x02\n\x02\x01\t\x00\x0cLibraAccount\x12WithdrawCapability\x1bextract_withdraw_capability\x08pay_from\x1brestore_withdraw_capability\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x01\x01\x01\x04\x01\x0c\x0b\x00\x11\x00\x0c\x05\x0e\x05\n\x01\n\x02\x0b\x03\x0b\x048\x00\x0b\x05\x11\x02\x02',
  'preburn' : b'\xa1\x1c\xeb\x0b\x01\x00\x00\x00\x07\x01\x00\x02\x02\x02\x04\x03\x06\x10\x04\x16\x02\x05\x18\x15\x07-`\x08\x8d\x01\x10\x00\x00\x00\x01\x01\x00\x00\x02\x00\x01\x00\x00\x03\x02\x03\x01\x01\x00\x04\x01\x03\x00\x01\x05\x01\x06\x0c\x01\x08\x00\x03\x06\x0c\x06\x08\x00\x03\x00\x02\x06\x0c\x03\x01\t\x00\x0cLibraAccount\x12WithdrawCapability\x1bextract_withdraw_capability\x07preburn\x1brestore_withdraw_capability\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x01\x01\x01\x04\x01\n\n\x00\x11\x00\x0c\x02\x0b\x00\x0e\x02\n\x018\x00\x0b\x02\x11\x02\x02',
  'publish_account_limit_definition' : b'\xa1\x1c\xeb\x0b\x01\x00\x00\x00\x06\x01\x00\x02\x03\x02\x06\x04\x08\x02\x05\n\x07\x07\x11*\x08;\x10\x00\x00\x00\x01\x00\x01\x01\x01\x00\x02\x01\x06\x0c\x00\x01\t\x00\rAccountLimits\x1bpublish_unrestricted_limits\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x01\x01\x01\x00\x01\x03\x0b\x008\x00\x02',
  'publish_shared_ed25519_public_key' : b'\xa1\x1c\xeb\x0b\x01\x00\x00\x00\x05\x01\x00\x02\x03\x02\x05\x05\x07\x06\x07\r\x1f\x08,\x10\x00\x00\x00\x01\x00\x01\x00\x02\x06\x0c\n\x02\x00\x16SharedEd25519PublicKey\x07publish\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x01\x00\x00\x01\x04\x0b\x00\x0b\x01\x11\x00\x02',
  'register_validator_config' : b'\xa1\x1c\xeb\x0b\x01\x00\x00\x00\x05\x01\x00\x02\x03\x02\x05\x05\x07\x0f\x07\x16\x1b\x081\x10\x00\x00\x00\x01\x00\x01\x00\x07\x06\x0c\x05\n\x02\n\x02\n\x02\n\x02\n\x02\x00\x0fValidatorConfig\nset_config\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x01\x00\x00\x01\t\x0b\x00\n\x01\x0b\x02\x0b\x03\x0b\x04\x0b\x05\x0b\x06\x11\x00\x02',
  'remove_validator_and_reconfigure' : b"\xa1\x1c\xeb\x0b\x01\x00\x00\x00\x05\x01\x00\x06\x03\x06\x0f\x05\x15\x18\x07-_\x08\x8c\x01\x10\x00\x00\x00\x01\x00\x02\x01\x03\x00\x01\x00\x02\x04\x02\x03\x00\x00\x05\x04\x01\x00\x02\x06\x0c\x03\x00\x01\x05\x01\n\x02\x02\x06\x0c\x05\x04\x06\x0c\x03\n\x02\x05\x02\x01\x03\x0bLibraSystem\x0cSlidingNonce\x0fValidatorConfig\x15record_nonce_or_abort\x0eget_human_name\x10remove_validator\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x01\x00\x05\x06\x12\n\x00\n\x01\x11\x00\n\x03\x11\x01\x0b\x02!\x0c\x04\x0b\x04\x03\x0e\x0b\x00\x01\x06\x00\x00\x00\x00\x00\x00\x00\x00'\x0b\x00\n\x03\x11\x02\x02",
  'rotate_authentication_key' : b"\xa1\x1c\xeb\x0b\x01\x00\x00\x00\x06\x01\x00\x04\x02\x04\x04\x03\x08\x19\x05! \x07A\xaf\x01\x08\xf0\x01\x10\x00\x00\x00\x01\x00\x03\x01\x00\x01\x02\x00\x01\x00\x00\x04\x00\x02\x00\x00\x05\x03\x04\x00\x00\x06\x02\x05\x00\x00\x07\x06\x05\x00\x01\x06\x0c\x01\x05\x01\x08\x00\x01\x06\x08\x00\x01\x06\x05\x00\x02\x06\x08\x00\n\x02\x02\x06\x0c\n\x02\x03\x08\x00\x01\x03\x0cLibraAccount\x06Signer\naddress_of\x15KeyRotationCapability\x1fextract_key_rotation_capability\x1fkey_rotation_capability_address\x1frestore_key_rotation_capability\x19rotate_authentication_key\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x01\x00\x07\x08\x14\n\x00\x11\x01\x0c\x02\x0e\x02\x11\x02\x14\x0b\x00\x11\x00!\x0c\x03\x0b\x03\x03\x0e\x06\x00\x00\x00\x00\x00\x00\x00\x00'\x0e\x02\x0b\x01\x11\x04\x0b\x02\x11\x03\x02",
  'rotate_authentication_key_with_nonce' : b'\xa1\x1c\xeb\x0b\x01\x00\x00\x00\x06\x01\x00\x04\x02\x04\x04\x03\x08\x14\x05\x1c\x17\x073\xa0\x01\x08\xd3\x01\x10\x00\x00\x00\x01\x00\x03\x01\x00\x01\x02\x00\x01\x00\x00\x04\x02\x03\x00\x00\x05\x03\x01\x00\x00\x06\x04\x01\x00\x02\x06\x0c\x03\x00\x01\x06\x0c\x01\x08\x00\x02\x06\x08\x00\n\x02\x03\x06\x0c\x03\n\x02\x0cLibraAccount\x0cSlidingNonce\x15record_nonce_or_abort\x15KeyRotationCapability\x1fextract_key_rotation_capability\x1frestore_key_rotation_capability\x19rotate_authentication_key\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x01\x00\x05\x03\x0c\n\x00\n\x01\x11\x00\x0b\x00\x11\x01\x0c\x03\x0e\x03\x0b\x02\x11\x03\x0b\x03\x11\x02\x02',
  'rotate_authentication_key_with_recovery_address' : b'\xa1\x1c\xeb\x0b\x01\x00\x00\x00\x05\x01\x00\x02\x03\x02\x05\x05\x07\x08\x07\x0f*\x089\x10\x00\x00\x00\x01\x00\x01\x00\x04\x06\x0c\x05\x05\n\x02\x00\x0fRecoveryAddress\x19rotate_authentication_key\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x01\x00\x00\x01\x06\x0b\x00\n\x01\n\x02\x0b\x03\x11\x00\x02',
  'rotate_dual_attestation_info' : b'\xa1\x1c\xeb\x0b\x01\x00\x00\x00\x05\x01\x00\x02\x03\x02\n\x05\x0c\r\x07\x19=\x08V\x10\x00\x00\x00\x01\x00\x01\x00\x00\x02\x00\x01\x00\x02\x06\x0c\n\x02\x00\x03\x06\x0c\n\x02\n\x02\x0fDualAttestation\x0frotate_base_url\x1crotate_compliance_public_key\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x01\x00\x02\x01\x07\n\x00\x0b\x01\x11\x00\x0b\x00\x0b\x02\x11\x01\x02',
  'rotate_shared_ed25519_public_key' : b'\xa1\x1c\xeb\x0b\x01\x00\x00\x00\x05\x01\x00\x02\x03\x02\x05\x05\x07\x06\x07\r"\x08/\x10\x00\x00\x00\x01\x00\x01\x00\x02\x06\x0c\n\x02\x00\x16SharedEd25519PublicKey\nrotate_key\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x01\x00\x00\x01\x04\x0b\x00\x0b\x01\x11\x00\x02',
  'set_validator_config_and_reconfigure' : b'\xa1\x1c\xeb\x0b\x01\x00\x00\x00\x05\x01\x00\x04\x03\x04\n\x05\x0e\x13\x07!E\x08f\x10\x00\x00\x00\x01\x01\x02\x00\x01\x00\x00\x03\x02\x01\x00\x07\x06\x0c\x05\n\x02\n\x02\n\x02\n\x02\n\x02\x00\x02\x06\x0c\x05\x0bLibraSystem\x0fValidatorConfig\nset_config\x1dupdate_config_and_reconfigure\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x01\x00\x00\x01\x0c\n\x00\n\x01\x0b\x02\x0b\x03\x0b\x04\x0b\x05\x0b\x06\x11\x00\x0b\x00\n\x01\x11\x01\x02',
  'set_validator_operator' : b"\xa1\x1c\xeb\x0b\x01\x00\x00\x00\x05\x01\x00\x04\x03\x04\n\x05\x0e\x13\x07!D\x08e\x10\x00\x00\x00\x01\x01\x02\x00\x01\x00\x00\x03\x02\x03\x00\x01\x05\x01\n\x02\x02\x06\x0c\x05\x00\x03\x06\x0c\n\x02\x05\x02\x01\x03\x0fValidatorConfig\x17ValidatorOperatorConfig\x0eget_human_name\x0cset_operator\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x01\x00\x04\x05\x0f\n\x02\x11\x00\x0b\x01!\x0c\x03\x0b\x03\x03\x0b\x0b\x00\x01\x06\x00\x00\x00\x00\x00\x00\x00\x00'\x0b\x00\n\x02\x11\x01\x02",
  'testnet_mint' : b"\xa1\x1c\xeb\x0b\x01\x00\x00\x00\x08\x01\x00\x08\x02\x08\x04\x03\x0c%\x041\x04\x055(\x07]\xc1\x01\x08\x9e\x02\x10\x06\xae\x02\x16\x00\x00\x00\x01\x00\x02\x00\x03\x02\x07\x01\x00\x00\x04\x00\x01\x00\x03\x05\x02\x03\x00\x01\x06\x01\x01\x01\x01\x02\x08\x03\x04\x00\x02\t\x02\x05\x00\x02\n\x06\x00\x01\x01\x02\x0b\x05\x00\x00\x02\t\x05\t\x00\x01\x03\x01\x06\x0c\x01\x05\x01\x01\x01\x08\x00\x05\x06\x08\x00\x05\x03\n\x02\n\x02\x03\x06\x0c\x05\x03\x07\x08\x00\x01\x03\x01\x03\x01\x03\x01\t\x00\x0fDualAttestation\x05Libra\x0cLibraAccount\x06Signer\x18get_cur_microlibra_limit\naddress_of\x14approx_lbr_for_value\x12WithdrawCapability\texists_at\x1bextract_withdraw_capability\x08pay_from\x1brestore_withdraw_capability\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x01\x05\x10\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\xdd\n\x02\x01\x00\x01\x01\x07\x08+\n\x01\x11\x03\x0c\x04\x0b\x04\x03\t\x0b\x00\x01\x06\xcb\x15z\x00\x00\x00\x00\x00'\n\x00\x11\x01\x07\x00!\x0c\x06\x0b\x06\x03\x14\x0b\x00\x01\x06\xcc\x15z\x00\x00\x00\x00\x00'\n\x028\x00\x11\x00#\x0c\x08\x0b\x08\x03\x1f\x0b\x00\x01\x06\xcd\x15z\x00\x00\x00\x00\x00'\x0b\x00\x11\x04\x0c\x03\x0e\x03\n\x01\n\x02\x07\x01\x07\x018\x01\x0b\x03\x11\x06\x02",
  'tiered_mint' : b'\xa1\x1c\xeb\x0b\x01\x00\x00\x00\x06\x01\x00\x04\x03\x04\x0b\x04\x0f\x02\x05\x11\x15\x07&<\x08b\x10\x00\x00\x00\x01\x01\x02\x00\x01\x00\x00\x03\x02\x01\x01\x01\x01\x04\x02\x06\x0c\x03\x00\x04\x06\x0c\x05\x03\x03\x05\x06\x0c\x03\x05\x03\x03\x01\t\x00\x0cLibraAccount\x0cSlidingNonce\x15record_nonce_or_abort\x0btiered_mint\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x01\x01\x01\x03\x01\t\n\x00\n\x01\x11\x00\x0b\x00\n\x02\n\x03\n\x048\x00\x02',
  'unfreeze_account' : b'\xa1\x1c\xeb\x0b\x01\x00\x00\x00\x05\x01\x00\x04\x03\x04\n\x05\x0e\x0e\x07\x1cD\x08`\x10\x00\x00\x00\x01\x00\x02\x00\x01\x00\x01\x03\x02\x01\x00\x02\x06\x0c\x05\x00\x02\x06\x0c\x03\x03\x06\x0c\x03\x05\x0fAccountFreezing\x0cSlidingNonce\x10unfreeze_account\x15record_nonce_or_abort\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x01\x00\x03\x01\x07\n\x00\n\x01\x11\x01\x0b\x00\n\x02\x11\x00\x02',
  'unmint_lbr' : b'\xa1\x1c\xeb\x0b\x01\x00\x00\x00\x06\x01\x00\x02\x02\x02\x04\x03\x06\x0f\x05\x15\x10\x07%e\x08\x8a\x01\x10\x00\x00\x00\x01\x01\x00\x00\x02\x00\x01\x00\x00\x03\x01\x02\x00\x00\x04\x03\x02\x00\x01\x06\x0c\x01\x08\x00\x00\x02\x06\x08\x00\x03\x02\x06\x0c\x03\x0cLibraAccount\x12WithdrawCapability\x1bextract_withdraw_capability\x1brestore_withdraw_capability\x0cunstaple_lbr\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x01\x00\x04\x01\t\x0b\x00\x11\x00\x0c\x02\x0e\x02\n\x01\x11\x02\x0b\x02\x11\x01\x02',
  'update_account_limit_definition' : b'\xa1\x1c\xeb\x0b\x01\x00\x00\x00\x06\x01\x00\x04\x03\x04\x0b\x04\x0f\x02\x05\x11\x19\x07*J\x08t\x10\x00\x00\x00\x01\x00\x02\x00\x01\x01\x01\x01\x03\x02\x01\x00\x00\x04\x06\x06\x0c\x05\x03\x03\x03\x03\x00\x02\x06\x0c\x03\x07\x06\x0c\x05\x03\x03\x03\x03\x03\x01\t\x00\rAccountLimits\x0cSlidingNonce\x18update_limits_definition\x15record_nonce_or_abort\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x01\x01\x01\x03\x01\x0b\n\x00\n\x02\x11\x01\x0b\x00\n\x01\n\x03\n\x04\n\x05\n\x068\x00\x02',
  'update_account_limit_window_info' : b'\xa1\x1c\xeb\x0b\x01\x00\x00\x00\x06\x01\x00\x02\x03\x02\x06\x04\x08\x02\x05\n\n\x07\x14!\x085\x10\x00\x00\x00\x01\x00\x01\x01\x01\x00\x02\x04\x06\x0c\x05\x03\x05\x00\x01\t\x00\rAccountLimits\x12update_window_info\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x01\x01\x01\x00\x01\x06\x0b\x00\n\x01\n\x02\n\x038\x00\x02',
  'update_dual_attestation_limit' : b'\xa1\x1c\xeb\x0b\x01\x00\x00\x00\x05\x01\x00\x04\x03\x04\n\x05\x0e\n\x07\x18H\x08`\x10\x00\x00\x00\x01\x00\x02\x00\x01\x00\x01\x03\x00\x01\x00\x02\x06\x0c\x03\x00\x03\x06\x0c\x03\x03\x0fDualAttestation\x0cSlidingNonce\x14set_microlibra_limit\x15record_nonce_or_abort\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x01\x00\x02\x01\x07\n\x00\n\x01\x11\x01\x0b\x00\n\x02\x11\x00\x02',
  'update_exchange_rate' : b'\xa1\x1c\xeb\x0b\x01\x00\x00\x00\x07\x01\x00\x06\x02\x06\x04\x03\n\x10\x04\x1a\x02\x05\x1c\x19\x075d\x08\x99\x01\x10\x00\x00\x00\x01\x00\x02\x00\x00\x02\x00\x00\x03\x00\x01\x00\x02\x04\x02\x03\x00\x01\x05\x04\x03\x01\x01\x02\x06\x02\x03\x03\x01\x08\x00\x02\x06\x0c\x03\x00\x02\x06\x0c\x08\x00\x04\x06\x0c\x03\x03\x03\x01\t\x00\x0cFixedPoint32\x05Libra\x0cSlidingNonce\x14create_from_rational\x15record_nonce_or_abort\x18update_lbr_exchange_rate\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x01\x01\x01\x05\x01\x0b\n\x00\n\x01\x11\x01\n\x02\n\x03\x11\x00\x0c\x04\x0b\x00\x0b\x048\x00\x02',
  'update_libra_version' : b'\xa1\x1c\xeb\x0b\x01\x00\x00\x00\x05\x01\x00\x04\x03\x04\n\x05\x0e\n\x07\x184\x08L\x10\x00\x00\x00\x01\x00\x02\x00\x01\x00\x01\x03\x00\x01\x00\x02\x06\x0c\x03\x00\x03\x06\x0c\x03\x03\x0cLibraVersion\x0cSlidingNonce\x03set\x15record_nonce_or_abort\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x01\x00\x02\x01\x07\n\x00\n\x01\x11\x01\x0b\x00\n\x02\x11\x00\x02',
  'update_minting_ability' : b'\xa1\x1c\xeb\x0b\x01\x00\x00\x00\x06\x01\x00\x02\x03\x02\x06\x04\x08\x02\x05\n\x08\x07\x12\x1d\x08/\x10\x00\x00\x00\x01\x00\x01\x01\x01\x00\x02\x02\x06\x0c\x01\x00\x01\t\x00\x05Libra\x16update_minting_ability\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x01\x01\x01\x00\x01\x04\x0b\x00\n\x018\x00\x02',
}