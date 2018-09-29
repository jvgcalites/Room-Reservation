# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Login.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost! 

from PyQt5.QtWidgets import QApplication, QDialog, QMessageBox
from PyQt5.uic import loadUi
import Login_Filehandling
import signUp
class Login(QDialog):
    
    def __init__(self):
        super(Login, self).__init__()
        loadUi('Login.ui',self)
        self.loginMsg = QMessageBox()
        self.setWindowTitle('Login')
      
        self.lfh = Login_Filehandling.Login_fileHandling()  
        #Button Events
        self.pushButton_login.clicked.connect(self.Login_Clicked)
        self.createAccount_commandLinkButton.clicked.connect(self.Signup_Clicked)

    def Login_Clicked(self):
        if self.lfh.LoadDatabase() is True:
            if self.lineEdit_userName.text() == '' or self.lineEdit_password.text() == '':
                self.label_state.setText("Please complete all fields!")
            else:
                if self.lfh.GetPasswordByEmail(self.lineEdit_userName.text()) == -1:
                  self.label_state.setText("Invalid Credentials")
                  self.lineEdit_userName.clear()
                  self.lineEdit_password.clear()
                else:
                    if self.lineEdit_password.text() != self.lfh.GetPasswordByEmail(self.lineEdit_userName.text()):
                        self.label_state.setText("Incorrect Password!")
                        self.lineEdit_password.clear()
                    else:
                        self.label_state.clear()
                        self.loginMsg.setText('Login Successful!')
                        self.loginMsg.exec_()
                        if self.lfh.AccountType(self.lineEdit_userName.text())=="Admin":
                           print('Admin')
                        else:
                           print('User')
                        self.lineEdit_userName.clear()
                        self.lineEdit_password.clear()
        else:
            print("Program Exits")         
            
        #Close Database
        self.lfh.CloseDatabase()                     
    def Signup_Clicked(self):
        self.close() #Closes Login window
        signUpWindow = signUp.signUp()
        signUpWindow.exec_()
    
if __name__ == "__main__":
    import sys
    app = QApplication(sys.argv)
    widget = Login()
    widget.show()
    sys.exit(app.exec_())

