# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Login.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost! 

from PyQt5.QtWidgets import QApplication, QWidget, QMessageBox
from PyQt5.uic import loadUi

class Accounts(QWidget):
    
    def __init__(self):
        super(Accounts, self).__init__()
        loadUi('Accounts.ui',self)
        self.loginMsg = QMessageBox()
        self.setWindowTitle('Room Reservation')

        #Button Events
        self.pushButton_SaveChanges.clicked.connect(self.SaveChanges_Clicked)
        self.pushButton_ActivateEditMode.clicked.connect(self.ActivateEditMode_Clicked)
        self.pushButton_Search.clicked.connect(self.Search_Clicked)
        self.pushButton_RemoveAccount.clicked.connect(self.RemoveAccount_Clicked)
        
    def SaveChanges_Clicked(self):
        print('Save')
    def ActivateEditMode_Clicked(self):
        self.pushButton_SaveChanges.setEnabled(True)      
        #Activate the Line Edit for corrections
        self.lineEdit_Surname.setDisabled(False)
        self.lineEdit_GivenName.setDisabled(False)
        self.lineEdit_MiddleName.setDisabled(False)
        self.lineEdit_EmailAddress.setDisabled(False)
        self.lineEdit_Password.setDisabled(False)
        self.lineEdit_UserID.setDisabled(False)
        self.lineEdit_ContactNumber.setDisabled(False)
        self.lineEdit_Organization.setDisabled(False)
    def Search_Clicked(self):
        print('Search')
    def RemoveAccount_Clicked(self):
        print('Remove')
    
if __name__ == "__main__":
    import sys
    app = QApplication(sys.argv)
    widget = Accounts()
    widget.show()
    sys.exit(app.exec_())

