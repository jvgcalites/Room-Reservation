# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Login.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost! 
import sys
sys.path.append('../')
from BusinessLogic.AccountsBL import AccountsBL
#from DataAccess.AccountsFilehandling import AccountsFileHandling
from PyQt5.QtWidgets import QApplication, QWidget, QMessageBox
from PyQt5.uic import loadUi
class Accounts(QWidget):
    
    def __init__(self):
        super(Accounts, self).__init__()
        loadUi('../UserInterface/Accounts.ui',self)
        self.loginMsg = QMessageBox()
        self.setWindowTitle('Room Reservation')
        self.ahl = AccountsBL()
#        self.ahl = AccountsFileHandling()
        #Button Events
        self.pushButton_SaveChanges.clicked.connect(self.SaveChanges_Clicked)
        self.pushButton_ActivateEditMode.clicked.connect(self.ActivateEditMode_Clicked)
        self.pushButton_Search.clicked.connect(self.Search_Clicked)
        self.pushButton_RemoveAccount.clicked.connect(self.RemoveAccount_Clicked)
        
        
    def SaveChanges_Clicked(self):
        self.ahl.LoadDatabase()
        if self.ahl.EmailExists(self.lineEdit_EmailAddress.text()):
            self.ahl.UpdateDatabase(self.lineEdit_Surname.text(),
                                    self.lineEdit_GivenName.text(),
                                    self.lineEdit_MiddleName.text(),
                                    self.lineEdit_EmailAddress.text(),
                                    self.lineEdit_Password.text(),
                                    self.lineEdit_Organization.text(),
                                    self.lineEdit_StudentNumber.text(),
                                    self.lineEdit_ContactNumber.text(),
                                    self.lineEdit_UserID.text())
            
            self.loginMsg.setText("Updated Sucessfully!")
            self.loginMsg.exec_()
            self.DisableLineEdits(True)
            self.ClearLineEdit()
            self.lineEdit_StudentNumber.clear()
            self.pushButton_SaveChanges.setDisabled(True)
        else:
            self.loginMsg.setText("Email address already exists!")
            self.loginMsg.exec_()
        self.ahl.CloseDatabase()
        
    def RemoveAccount_Clicked(self):
        
        self.ahl.LoadDatabase()
        self.ahl.RemoveAccount(self.lineEdit_UserID.text())
        self.ahl.CloseDatabase()
        self.loginMsg.setText("Account Removed Sucessfully!")
        self.loginMsg.exec_()
    def ActivateEditMode_Clicked(self):
        self.pushButton_SaveChanges.setEnabled(True)      
        #Activate the Line Edit for corrections
        self.DisableLineEdits(False)
    def Search_Clicked(self):
#        self.ahl.LoadDatabase()
        studentNumber = self.lineEdit_StudentNumber.text()
        value = []        
        if self.ahl.studentNumberExists(studentNumber):
            self.lineEdit_StudentNumber.setText(studentNumber.replace(' ',''))
            value = self.ahl.getDataByStudentNumber(studentNumber)
            self.DisableLineEdits(True)
            self.pushButton_ActivateEditMode.setEnabled(True)
            self.pushButton_RemoveAccount.setEnabled(True)
            self.lineEdit_Surname.setText(value[0][0])
            self.lineEdit_GivenName.setText(value[0][1])
            self.lineEdit_MiddleName.setText(value[0][2])
            self.lineEdit_EmailAddress.setText(value[0][3])
            self.lineEdit_UserID.setText(value[0][5])
            self.lineEdit_ContactNumber.setText(value[0][7])
            self.lineEdit_Organization.setText(value[0][4])
            self.lineEdit_Password.setText(self.ahl.getPasswordByStudentNumber(studentNumber))
          
        else:
            self.lineEdit_StudentNumber.clear()
            self.pushButton_ActivateEditMode.setEnabled(False)
            self.pushButton_RemoveAccount.setEnabled(False)
            #Clear Content
            self.ClearLineEdit()
            self.pushButton_ActivateEditMode.setEnabled(False)
            self.pushButton_RemoveAccount.setEnabled(False)
            #Clear Content
            ##################################################################
            self.pushButton_SaveChanges.setEnabled(False) #Disable button
            ###################################################################
            self.loginMsg.setText(self.ahl.showStateOfStudentNumber(self.lineEdit_StudentNumber.text()))            
            self.loginMsg.exec_()
     
    #Disables line Edits 
    def DisableLineEdits(self, state):
        self.lineEdit_Surname.setDisabled(state)
        self.lineEdit_GivenName.setDisabled(state)
        self.lineEdit_MiddleName.setDisabled(state)
        self.lineEdit_EmailAddress.setDisabled(state)
        self.lineEdit_Password.setDisabled(state)
        self.lineEdit_UserID.setDisabled(True)
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
        
    
if __name__ == "__main__":
    import sys
    app = QApplication(sys.argv)
    widget = Accounts()
    widget.show()
    sys.exit(app.exec_())

