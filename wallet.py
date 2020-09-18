#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File    :   wallet.py
@Time    :   2020/09/16 16:43:09
@Author  :   Guo Yi 
@Version :   0.1
@Contact :   guoyi1026@gmail.com
@License :   (C)Copyright 2020
@Desc    :   None
'''

# here put the import lib

from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *

import uuid
import time
import os
import traceback, sys

from libra_client.wallet_library import WalletLibrary
from libra_client.client import Client


class TransactionHistoryTableModel(QAbstractTableModel):
    """
    keep the method names
    they are an integral part of the model
    """
    def __init__(self, parent, MySnapshot_list, header, *args):
        QAbstractTableModel.__init__(self, parent, *args)
        #finalData = MySnapshot_list
        #for eachRecord in MySnapshot_list:
            
        #    finalData.append(thisRecord)

        self.mylist = MySnapshot_list
        self.header = ["Txid","From", "To", "Amount"]

    def rowCount(self, parent):
        return len(self.mylist)

    def columnCount(self, parent):
        if len(self.mylist) > 0:
            return len(self.mylist[0])
        return 0
        
    def data(self, index, role):
        if not index.isValid():
            return None
        value = self.mylist[index.row()][index.column()]
        if role == Qt.EditRole:
            return value
        elif role == Qt.DisplayRole:
            return value

    def headerData(self, col, orientation, role):
        if orientation == Qt.Horizontal and role == Qt.DisplayRole:
            return self.header[col]
        return None



class MainWindow(QMainWindow):
    def __init__(self, *args, **kwargs):
        super(MainWindow, self).__init__(*args, **kwargs)
      
        layout = QVBoxLayout()
        self.rootLayout = layout

        self.file_name = "test.key"

        file_layout = QHBoxLayout()
        self.file_label = QLabel("test.key")
        file_layout.addWidget(QLabel("Current wallet file: "))
        file_layout.addWidget(self.file_label)
        file_widget = QWidget()
        file_widget.setLayout(file_layout)

        
        #钱包
        wallet_layout = QHBoxLayout()
        b = QPushButton("Open Wallet file")
        b.pressed.connect(self.open_file)
        wallet_layout.addWidget(b)
        new_wallet_btn = QPushButton("Create Wallet file")
        new_wallet_btn.pressed.connect(self.pop_create_wallet_window)
        wallet_layout.addWidget(new_wallet_btn)
        wallet_widget = QWidget()
        wallet_widget.setLayout(wallet_layout)


        balance_widget = self.create_balance_widget()

        layout.addWidget(file_widget)
        layout.addWidget(wallet_widget)
        layout.addWidget(balance_widget)
        
        self.w = QWidget()
        self.w.setLayout(layout)
        self.w.setFixedSize(800,600)
        self.w.setWindowTitle("Core Wallet")
        self.w.show()

        self.wallet =WalletLibrary.recover(self.file_name)
        ## libra testnet
        self.libra_client = Client("testnet") 
        self.open_selected_wallet()

        self.threadPool = QThreadPool()
        self.threadPool.setMaxThreadCount(8)
        print("Multithreading with maximum %d threads" % self.threadPool.maxThreadCount())
        
    def open_file(self):
        file_name_selected = QFileDialog.getOpenFileName(self, "QFileDialog.getOpenFileName()", "","key Files (*.key);;All Files (*)")
        file_name = file_name_selected[0]
        fileter   = file_name_selected[1]
        if(file_name == ''):
            print("User cancel file")
        else:
            print("User select file with %s" % file_name)
            self.file_name = file_name
            self.wallet =WalletLibrary.recover(self.file_name)
            self.open_selected_wallet()
            #self.w.close()

    def select_file_for_create_wallet(self):
        file_name_selected = QFileDialog.getSaveFileName(self, "QFileDialog.getOpenFileName()", "","key Files (*.key);;All Files (*)")
        file_name = file_name_selected[0]
        fileter   = file_name_selected[1]
        if(file_name == ''):
            print("User cancel file")
        else:
            print("User select file with %s" % file_name)
            self.file_selected_edit.setText(file_name)

    # 生成钱包，存储到文件
    def create_account_pressed(self):
        self.user_input_file = self.file_selected_edit.text()
        print(self.user_input_file)
        # Create a new random wallet
        self.wallet = WalletLibrary.new()
        self.wallet.new_account()
        print(self.wallet.mnemonic)
        self.wallet.write_recovery(self.user_input_file)

        self.go_create_accout_btn.setDisabled(True)
        self.open_selected_wallet()
        self.create_account_widget.close()
        

    def pop_create_wallet_window(self):

        file_selection_layout = QHBoxLayout()
        file_title_widget = QLabel("Wallet file name:")
        self.file_selected_edit     = QLineEdit()
        file_browser_btn  = QPushButton("Select wallet file name")
        file_browser_btn.pressed.connect(self.select_file_for_create_wallet)
        file_selection_layout.addWidget(file_title_widget)
        file_selection_layout.addWidget(self.file_selected_edit)
        file_selection_layout.addWidget(file_browser_btn)
        file_title_selection_widget = QWidget()
        file_title_selection_widget.setLayout(file_selection_layout)


        self.create_account_progress_widget = QLabel("Progress")
        self.create_account_progress_widget.setAlignment(Qt.AlignCenter)

        go_create_accout_btn  = QPushButton("Create wallet")
        go_create_accout_btn.pressed.connect(self.create_account_pressed)
        self.go_create_accout_btn = go_create_accout_btn
        

        create_account_layout = QVBoxLayout()
        create_account_layout.addWidget(file_title_selection_widget)
        create_account_layout.addWidget(go_create_accout_btn)
        create_account_layout.addWidget(self.create_account_progress_widget)

        self.create_account_layout = create_account_layout

        self.create_account_widget = QWidget()
        self.create_account_widget.setLayout(create_account_layout)
        self.create_account_widget.show()

    
    def get_faucet_pressed(self):
        self.libra_client.mint_coins(self.account.address, self.account.auth_key_prefix, 1_123_000, is_blocking=True)
        balance0 = self.libra_client.get_balance(self.address, retry=True)
        print('balance0 ',balance0)
        self.balance_label.setText(str(balance0))

    def send_asset_to_address(self):
        toaddress = self.send_address.text()
        amountstr = self.send_amount.text()
 
        if len(toaddress) != 32:
            QMessageBox.about(self,"error","to address error")
        elif amountstr.isdigit() == False:
            QMessageBox.about(self,"error","amount error")
        else:
            toamount = int(amountstr)
            print('From ', self.address, 'To ', toaddress, ' Amount:',toamount)
            ret = self.libra_client.transfer_coin(self.account, toaddress, toamount, gas_unit_price=1, is_blocking=True)
            balance0 = self.libra_client.get_balance(self.address, retry=True)
            print('-- balance0 ',balance0)
            QMessageBox.about(self,"info","send asset successful")
    
    def update_transaction_history(self):
        #pass
        header = ["Txid","From", "To", "Amount"]
        #get transaction history
        ret_trans = self.libra_client.get_account_transactions(self.address, 0,1000)
        self.all_transaction_history_list = []
        for tran in ret_trans:
            history_one = []
            history_one.append(tran.version)
            history_one.append(tran.transaction.sender)
            history_one.append(tran.transaction.script.receiver)
            history_one.append(tran.transaction.script.amount)
            self.all_transaction_history_list.append(history_one)

        this_tableModel = TransactionHistoryTableModel(None, self.all_transaction_history_list, header)
        self.history_table.setModel(this_tableModel)
        self.history_table.update()
        if len(self.all_transaction_history_list) > 0:
            header = self.history_table.horizontalHeader()       
            header.setSectionResizeMode(0, QHeaderView.ResizeToContents)
            header.setSectionResizeMode(1, QHeaderView.ResizeToContents)
            header.setSectionResizeMode(2, QHeaderView.ResizeToContents)
            header.setSectionResizeMode(3, QHeaderView.ResizeToContents)
            

    def tab_is_selected(self, index):
        print("tab is changed" + str(index))
        if index == 1:  
            self.update_transaction_history()


    def create_balance_widget(self):
        #钱包
        #地址
        address_layout = QHBoxLayout()
        self.address_label = QLabel("0")
        address_layout.addWidget(QLabel("Wallet Address: "))
        address_layout.addWidget(self.address_label)
        self.address_label.setTextInteractionFlags(Qt.TextSelectableByMouse);
        getfaucet_btn  = QPushButton("Get Faucet")
        getfaucet_btn.pressed.connect(self.get_faucet_pressed)
        address_layout.addSpacing(50)
        address_layout.addWidget(getfaucet_btn)


        address_widget = QWidget()
        address_widget.setLayout(address_layout)
        
        #余额
        balance_layout = QHBoxLayout()
        self.balance_label = QLabel("00")
        balance_layout.addWidget(QLabel("Wallet Balance: "))
        balance_layout.addWidget(self.balance_label)
        balance_widget = QWidget()
        balance_widget.setLayout(balance_layout)

        #发送
        #send widget:
        send_address_layout = QHBoxLayout()
        self.send_address = QLineEdit()
        send_address_layout.addWidget(QLabel("Send Address: "))
        send_address_layout.addWidget(self.send_address)
        send_address_widget = QWidget()
        send_address_widget.setLayout(send_address_layout)
        
        send_amount_layout = QHBoxLayout()
        self.send_amount = QLineEdit()
        send_amount_layout.addWidget(QLabel("Send Amount: "))
        send_amount_layout.addWidget(self.send_amount)
        send_amount_widget = QWidget()
        send_amount_widget.setLayout(send_amount_layout)
        
        self.send_asset = QPushButton("Send asset")
        self.send_asset.pressed.connect(self.send_asset_to_address)

        send_layout = QVBoxLayout()
        send_layout.addWidget(send_address_widget)
        send_layout.addWidget(send_amount_widget)
        send_layout.addWidget(self.send_asset)
        self.send_widget = QWidget()
        self.send_widget.setLayout(send_layout)

        #历史
        self.history_table  = QTableView()
        header = ["Txid","From", "To", "Amount"]
        self.all_transaction_history_list = []
        this_tableModel = TransactionHistoryTableModel(None, self.all_transaction_history_list, header)
        self.history_table.setModel(this_tableModel)

        self.account_tab_widget = QTabWidget()
        self.account_tab_widget.addTab(self.send_widget, "Send")
        self.account_tab_widget.addTab(self.history_table, "History")
        self.account_tab_widget.currentChanged.connect(self.tab_is_selected)


        asset_operation_layout = QVBoxLayout()
        asset_operation_layout.addWidget(address_widget)
        asset_operation_layout.addWidget(balance_widget)
        asset_operation_layout.addWidget(self.account_tab_widget)
       
        widget_balance = QWidget()
        widget_balance.setLayout(asset_operation_layout)
        
        return widget_balance
    
    def open_selected_wallet(self):
        #假定暂时只有1个
        self.account = self.wallet.accounts[0]
        self.address = self.account.address.hex()
        print('Account 0: \n Address:\t ',self.address)
       
        balance = self.libra_client.get_balance(self.account.address)
        print(balance)
        
        self.address_label.setText(self.address)
        self.balance_label.setText(str(balance))



if __name__ == "__main__":
    app = QApplication([])
    window = MainWindow()
    app.exec_()
