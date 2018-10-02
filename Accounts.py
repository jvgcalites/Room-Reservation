# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Login.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost! 

from PyQt5.QtWidgets import QApplication, QWidget, QMessageBox
from PyQt5.uic import loadUi
import AccountsFilehandling
class Accounts(QWidget):
    
    def __init__(self):
        super(Accounts, self).__init__()
        loadUi('Accounts.ui',self)
        self.loginMsg = QMessageBox()
        self.setWindowTitle('Room Reservation')
        self.ahl = AccountsFilehandling.AccountsFileHandling()
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
        self.DisableLineEdits(False)
    def Search_Clicked(self):
        self.ahl.LoadDatabase()
        value = self.ahl.GetDetailsByStudentNumber(self.lineEdit_StudentNumber.text())
        if len(self.lineEdit_StudentNumber.text()) != 10:
            self.loginMsg.setText("Student nubmer can't be less than 10 characters!")            
            self.loginMsg.exec_()
            self.lineEdit_StudentNumber.clear()
            #Clear Content
            self.ClearLineEdit()
            #Disable Save Changes button
            self.pushButton_SaveChanges.setEnabled(False)
            #Disable Line Edit
            self.DisableLineEdits(True)
            ###################################################################
        elif value != -1:
            self.lineEdit_Surname.setText(value[0][0])
            self.lineEdit_GivenName.setText(value[0][1])
            self.lineEdit_MiddleName.setText(value[0][2])
            self.lineEdit_EmailAddress.setText(value[0][3])
            self.lineEdit_UserID.setText(value[0][5])
            self.lineEdit_ContactNumber.setText(value[0][7])
            self.lineEdit_Organization.setText(value[0][4])
            ###################################################################
            self.lineEdit_Password.setText(self.ahl.GetPasswordByEmail(value[0][3]))
        else:
            #Clear Content
            self.ClearLineEdit()
            ##################################################################
            self.pushButton_SaveChanges.setEnabled(False) #Disable button
            ###################################################################
            self.loginMsg.setText("Student number does not exist")
            self.loginMsg.exec_()
            self.lineEdit_StudentNumber.clear()

        self.ahl.CloseDatabase()
    #Disables line Edits 
    def DisableLineEdits(self, state):
        self.lineEdit_Surname.setDisabled(state)
        self.lineEdit_GivenName.setDisabled(state)
        self.lineEdit_MiddleName.setDisabled(state)
        self.lineEdit_EmailAddress.setDisabled(state)
        self.lineEdit_Password.setDisabled(state)
        self.lineEdit_UserID.setDisabled(state)
        self.lineEdit_ContactNumber.setDisabled(state)
        self.lineEdit_Organization.setDisabled(state)       
        
    def ClearLineEdit(self):
        self.lineEdit_Surname.clear()
        self.lineEdit_GivenName.clear()
        self.lineEdit_MiddleName.clear()
        self.lineEdit_EmailAddress.clear()
        self.lineEdit_UserID.clear()
        self.lineEdit_ContactNumber.clear()
        self.lineEdit_Organization.clear()
        self.lineEdit_Password.clear()        
    def RemoveAccount_Clicked(self):
        print('Remove')
    
if __name__ == "__main__":
    import sys
    app = QApplication(sys.argv)
    widget = Accounts()
    widget.show()
    sys.exit(app.exec_())

