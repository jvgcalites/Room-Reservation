#!/usr/bin/env python
# -*- coding: utf-8 -*-
#import re    
import sys
from userInfo import UserInfo
from PyQt5.QtWidgets import QApplication, QDialog, QMessageBox
from PyQt5.uic import loadUi

class signUp(QDialog):
    def __init__(self):
        super(signUp, self).__init__()
        loadUi('signUp.ui', self)
        self.setWindowTitle('Sign Up')
        #Button Event
        self.pushButton_signUp.clicked.connect(self.SignUp_Done)
        
    def SignUp_Done(self):
        self.newUser = UserInfo()
        self.PassUserInfo()
        if self.newUser.IsComplete() == False:
            self.MessageBox("Please complete all fields", "Error")
        elif self.newUser.Check_Password() == False:
            self.MessageBox("Password must contain at least 8 characters and composed of an uppercase, lowercase, and a number", "Error")
        elif self.newUser.Check_StudentNumber() == False:
            self.MessageBox("Student number must contain 10 numbers", "Error")
        else:
            self.MessageBox("New Account Created Successfully", "Success")
            self.newUser.StoreInfo()
            self.CloseWindow()
              
    def PassUserInfo(self):
        self.newUser.SetLastName(self.lineEdit_lastName.text())
        self.newUser.SetGivenName(self.lineEdit_givenName.text())
        self.newUser.SetMiddleName(self.lineEdit_middleName.text())
        self.newUser.SetEmailAddress(self.lineEdit_emailAddress.text())
        self.newUser.SetPassword(self.lineEdit_password.text())
        self.newUser.SetOrganization(str(self.comboBox_organization.currentText()))
        self.newUser.SetStudentNumber(self.lineEdit_studentNumber.text())
        self.newUser.SetContactNumber(self.lineEdit_contactNum.text())
        self.newUser.SetUserType(self.UserType())

    def UserType(self):
        if self.radioButton_admin.isChecked() == True:
            return self.radioButton_admin.text()
        elif self.radioButton_User.isChecked() == True:
            return self.radioButton_User.text()
        else:
            return ""
        
    def MessageBox(self, message, windowTitle):
        
        msg = QMessageBox()
        msg.setText(message) #show passed message variable
        msg.setWindowTitle(windowTitle)
        msg.setStandardButtons(QMessageBox.Ok)
        msg.exec_()
        
    def CloseWindow(self):
        self.close()

if __name__ == '__main__': 
    app = QApplication(sys.argv)
    widget = signUp()
    widget.show()
    sys.exit(app.exec_())
   
