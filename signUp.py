#!/usr/bin/env python
# -*- coding: utf-8 -*-
import re    
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
        self.pushButton_signUp.clicked.connect(self.signUp_done)

    def signUp_done(self):
        msg = QMessageBox()
        #check if all blanks are filled up
        if self.isComplete() == False:
            msg.setText("Kindly fill up all the informations")
            msg.setWindowTitle("Error")
            msg.setStandardButtons(QMessageBox.Ok)
            msg.exec_()
        if self.isComplete() == True:
            print("good")
            #pass userInfo to database
            fh = Signup_fileHandling()
            fh.LoadDatabase()
            fh.InsertAccount(self.userInfo().lastName,
                             self.userInfo().givenName,
                             self.userInfo().middleName,
                             self.userInfo().emailAddress,
                             self.userInfo().password,
                             self.userInfo().organization,
                             self.userInfo().studentNumber,
                             self.userInfo().contactNumber
                             )
            fh.CloseDatabase()
            #show new window
            msg.setText("New account created successfully!")
            msg.setWindowTitle("Success")
            msg.setStandardButtons(QMessageBox.Ok)
            msg.exec_()  
            self.close()

    def userInfo(self):
        lname = self.lineEdit_lastName.text()
        gname = self.lineEdit_givenName.text()
        mname = self.lineEdit_middleName.text()
        email = self.lineEdit_emailAddress.text()
        pw= self.lineEdit_password.text()
        org = str(self.comboBox_organization.currentText())
        studNum = self.lineEdit_studentNumber.text()
        contactNum = self.lineEdit_contactNum.text()
        newUser = UserInfo(lname, gname, mname, email, pw, org, studNum, contactNum)
        return newUser
    
    def isComplete(self):
        x = True
        if self.lineEdit_lastName.text() == "":
            x = False
        if self.lineEdit_givenName.text() == "":
            x = False
        if self.lineEdit_middleName.text() == "":
            x = False
        if self.lineEdit_emailAddress.text() == "":
            x = False
        if self.check_password(self.lineEdit_password.text()) == "":
            self.lineEdit_password.clear()
            x = False
        if self.comboBox_organization.currentText() == "":
            x = False
        if self.check_studentNumber(self.lineEdit_studentNumber.text()) == "":
            self.lineEdit_studentNumber.clear()
            x = False
        if self.lineEdit_contactNum.text() == "":
            x = False
        return x
        
    def check_password(self, x):
        #minimum of 8 characters in length
        #at least 1 character of uppercase, lowercase, and digit
        if (len(x) < 8):
            return ""
        elif not re.search("[a-z]", x):
            return ""
        elif not re.search("[0-9]", x):
            return ""
        elif not re.search("[A-Z]", x):
            return ""
        else:
            return x
            print("valid password")
    
    def check_studentNumber(self, x):
        #student number contains 10 digits
        if (len(x) == 10 and x.isdigit()):
            return x
        else:
            return ""
            
        

        

if __name__ == '__main__': 
    app = QApplication(sys.argv)
    widget = signUp()
    widget.show()
    sys.exit(app.exec_())
    
