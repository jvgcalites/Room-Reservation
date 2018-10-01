#!/usr/bin/env python
# -*- coding: utf-8 -*-
#import re    
import sys
from Signup_Filehandling import Signup_fileHandling
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
        if self.newUser.isComplete() == False:
            self.MessageBox("Please complete all fields", "Error")
        elif self.newUser.check_password() == False:
            self.MessageBox("Password must contain at least 8 characters and composed of an uppercase, lowercase, and a number", "Error")
        elif self.newUser.check_studentNumber() == True:
            self.MessageBox("Student number must contain 10 numbers", "Error")
        else:
            self.MessageBox("New Account Created Successfully", "Success")
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
        print(self.newUser.GetLastName())
        print(self.newUser.GetGivenName())
        print(self.newUser.GetMiddleName())
        print(self.newUser.GetEmailAddress())
        print(self.newUser.GetPassword())
        print(self.newUser.GetOrganization())
        print(self.newUser.GetStudentNumber())
        print(self.newUser.GetContactNumber())
        print(self.newUser.GetUserType())
        
    def UserType(self):
        if self.radioButton_admin.isChecked() == True:
            return self.radioButton_admin.text()
        elif self.radioButton_user.isChecked() == True:
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
   
