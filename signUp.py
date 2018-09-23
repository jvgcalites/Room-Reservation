#!/usr/bin/env python
# -*- coding: utf-8 -*-
    
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
        if self.lineEdit_lastName.text() == "":
            return False
        elif self.lineEdit_givenName.text() == "":
            return False
        elif self.lineEdit_middleName.text() == "":
            return False
        elif self.lineEdit_emailAddress.text() == "":
            return False
        elif self.lineEdit_password.text() == "":
            return False
        elif self.comboBox_organization.currentText() == "":
            return False
        elif self.lineEdit_studentNumber.text() == "":
            return False
        elif self.lineEdit_contactNum.text() == "":
            return False
        else:
            return True
        

        

if __name__ == '__main__': 
    app = QApplication(sys.argv)
    widget = signUp()
    widget.show()
    sys.exit(app.exec_())
    
