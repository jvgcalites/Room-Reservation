#!/usr/bin/env python
# -*- coding: utf-8 -*-
import re    
import sys
from Signup_Filehandling import Signup_fileHandling
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
        
        #check if all blanks are filled up
        if self.isComplete() == False:
            self.errorMessage() # Show error message
            
        if self.isComplete() == True:
            #pass informations filled in to database
            fh = Signup_fileHandling()
            fh.LoadDatabase()
            fh.InsertAccount(self.lineEdit_lastName.text(),
                             self.lineEdit_givenName.text(),
                             self.lineEdit_middleName.text(),
                             self.lineEdit_emailAddress.text(),
                             self.lineEdit_password.text(),
                             str(self.comboBox_organization.currentText()),
                             self.lineEdit_studentNumber.text(),
                             self.lineEdit_contactNum.text(),
                             self.radioButton_User.text()
                             )
            fh.CloseDatabase()
            #show new window 
            msg = QMessageBox()
            msg.setText("New account created successfully!")
            msg.setWindowTitle("Success")
            msg.setStandardButtons(QMessageBox.Ok)
            msg.exec_()  
            self.close()
            
    # This function returns True if all fields are filled up correctly        
    def isComplete(self):
        
        if self.lineEdit_lastName.text() == "":
            x = False
        elif self.lineEdit_givenName.text() == "":
            x = False
        elif self.lineEdit_middleName.text() == "":
            x = False
        elif self.lineEdit_emailAddress.text() == "":
            x = False
        elif self.check_password(self.lineEdit_password.text()) == "":
            self.lineEdit_password.clear()
            x = False
        elif self.comboBox_organization.currentText() == "":
            x = False
        elif self.check_studentNumber(self.lineEdit_studentNumber.text()) == "":
            self.lineEdit_studentNumber.clear()
            x = False
        elif self.radioButton_admin.isChecked() == False and self.radioButton_User.isChecked() == False:
            x = False
        else:
            x = True
        # return True or False    
        return x 
      
    def errorMessage(self):
        #Check which cause the error, then pass a string to messageBox
        if self.lineEdit_lastName.text() == "":
            self.messageBox("Kindly fill up all the information")
        elif self.lineEdit_givenName.text() == "":
            self.messageBox("Kindly fill up all the information")
        elif self.lineEdit_middleName.text() == "":
            self.messageBox("Kindly fill up all the information")
        elif self.lineEdit_emailAddress.text() == "":
            self.messageBox("Kindly fill up all the information")
        elif self.check_password(self.lineEdit_password.text()) == "":
            self.messageBox("Password must contain at least 8 characters and composed of an uppercase, lowercase, and a number")
        elif self.comboBox_organization.currentText() == "":
            self.messageBox("Select an organization")
        elif self.check_studentNumber(self.lineEdit_studentNumber.text()) == "":
            self.messageBox("Student number must contain 10 numbers")
        elif self.radioButton_admin.isChecked() == False and self.radioButton_User.isChecked() == False:
            self.messageBox("Select admin or user")
        else:
            self.messageBox("Kindly fill up all the information")
    
    #Accepts string message and output it in a QMessageBox  
    def messageBox(self, message):
        
        msg = QMessageBox()
        msg.setText(message) #show passed message variable
        msg.setWindowTitle("Error")
        msg.setStandardButtons(QMessageBox.Ok)
        msg.exec_()
        
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
    
