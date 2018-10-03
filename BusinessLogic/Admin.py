#!/usr/bin/env python
# -*- coding: utf-8 -*-    

import sys
from PyQt5.QtWidgets import QApplication, QDialog, QMessageBox
from PyQt5.uic import loadUi
import Accounts

class Admin(QDialog):
    def __init__(self):
        super(Admin, self).__init__()
        loadUi('../UserInterface/Admin.ui', self)
        self.setWindowTitle('Admin')
        #Button Event
        self.pushButton_manageAccounts.clicked.connect(self.OpenAccounts)
        self.pushButton_manageSchedule.clicked.connect(self.OpenSchedule)
        
        
    def OpenAccounts(self):
        acc = Accounts.Accounts()
        acc.show()
        
    def OpenSchedule(self):
        ####################################################################
        print("Admin")
        #################################################################

if __name__ == '__main__': 
    app = QApplication(sys.argv)
    widget = Admin()
    widget.show()
    sys.exit(app.exec_())
   
