#!/usr/bin/env python
# -*- coding: utf-8 -*-    
import sys
sys.path.append('../')
from BusinessLogic.SignupBL import SignupBL
from PyQt5.QtWidgets import QApplication, QDialog, QMessageBox
from PyQt5.uic import loadUi

class Ui_SignUp(QDialog):
    def __init__(self):
        super(Ui_SignUp, self).__init__()
        loadUi('../UserInterface/signUp.ui', self)
        self.setWindowTitle('Sign Up')
        #Button Event
        self.pushButton_signUp.clicked.connect(self.SignUp_Done)
        
    def SignUp_Done(self):
        #intialize object
        self.newUser = SignupBL()
        #Set information to object
        self.PassUserInfo()
        #Check for errors
        if self.newUser.IsComplete() == False:
            self.MessageBox("Please complete all fields", "Error")
        elif self.newUser.Check_Password() == False:
            self.MessageBox("Password must contain at least 8 characters and composed of an uppercase, lowercase, and a number", "Error")
        elif self.newUser.Check_StudentNumber() == False:
            self.MessageBox("Student number must contain 10 numbers", "Error")
        else: #There is no error
            self.MessageBox("New Account Created Successfully", "Success")
            self.newUser.StoreInfo() #Store to Database
            self.CloseWindow()
              
    def PassUserInfo(self):
        self.newUser.lastName = self.lineEdit_lastName.text()
        self.newUser.givenName =self.lineEdit_givenName.text()
        self.newUser.middleName = self.lineEdit_middleName.text()
        self.newUser.userName = self.lineEdit_userName.text()
        self.newUser.emailAddress = self.lineEdit_emailAddress.text()
        self.newUser.password = self.lineEdit_password.text()
        self.newUser.organization = str(self.comboBox_organization.currentText())
        self.newUser.studentNumber = self.lineEdit_studentNumber.text()
        self.newUser.contactNumber = self.lineEdit_contactNum.text()
        self.newUser.userType = self.UserType()
    
    def UserType(self):
        if self.radioButton_admin.isChecked() == True:
            return "Admin"
        elif self.radioButton_User.isChecked() == True:
            return "User"
        else:
            return ""
        
    #Creates message box    
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
    widget = Ui_SignUp()
    widget.show()
    sys.exit(app.exec_())
   
