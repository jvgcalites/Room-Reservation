#!/usr/bin/env python
# -*- coding: utf-8 -*-    

import sys
sys.path.append('../')
from PyQt5.QtWidgets import QApplication, QDialog, QMessageBox
from PyQt5.uic import loadUi
import Accounts
import Schedule

class Admin(QDialog):
    def __init__(self):
        super(Admin, self).__init__()
        loadUi('../UserInterface/Admin.ui', self)
        self.setWindowTitle('Admin')
        #Button Event
        self.pushButton_manageAccounts.clicked.connect(self.OpenAccounts)
        self.pushButton_manageSchedule.clicked.connect(self.OpenSchedule)
        
        
    def OpenAccounts(self):
         self.acc = Accounts.Accounts()
         self.acc.show()
         self.close()

    def OpenSchedule(self):
        ####################################################################
        print("Admin")
        self.schedule = Schedule.Schedule()
        self.schedule.show()
        self.close()
        #################################################################

if __name__ == '__main__': 
    import sys
    app = QApplication(sys.argv)
    widget = Admin()
    widget.show()
    sys.exit(app.exec_())
   
20