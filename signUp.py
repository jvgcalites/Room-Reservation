#!/usr/bin/env python
# -*- coding: utf-8 -*-
    
import sys
from userInfo import UserInfo
from PyQt5.QtWidgets import QApplication, QDialog, QMessageBox
from PyQt5.uic import loadUi

class signUp(QDialog):
    def __init__(self):
        super(signUp, self).__init__()
        loadUi('signUp.ui', self)
        self.setWindowTitle('Sign Up')
        self.pushButton_signUp.clicked.connect(self.signUp_done)

    def signUp_done(self):
        #pass userInfo to database
        
        #show new window
        msg = QMessageBox()
        msg.setText("New Account Created")
        msg.setStandardButtons(QMessageBox.Ok)
        msg.exec_()  
        
    def userInfo(self):
        lname = self.lineEdit_lastName.text()
        gname = self.lineEdit_givenName.text()
        mname = self.lineEdit_middleName.text()
        pw= self.lineEdit_password.text()
        org = str(self.comboBox_organization.currentText())
        studNum = self.lineEdit_studentNumber.text()
        contactNum = self.lineEdit_contactNum.text()
        newUser = UserInfo(lname, gname, mname, pw, org, studNum, contactNum)
        return newUser
        

if __name__ == '__main__': 
    app = QApplication(sys.argv)
    widget = signUp()
    widget.show()
    sys.exit(app.exec_())
    
