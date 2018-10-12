# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Login.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost! 
import sys
sys.path.append('../')
from BusinessLogic.LoginBL import LoginBL
from PyQt5.QtWidgets import QApplication, QDialog, QMessageBox
from PyQt5.uic import loadUi
import signUp, User, Admin

class Ui_Login(QDialog):
    
    def __init__(self):
        super(Ui_Login, self).__init__()
        loadUi('../UserInterface/Login.ui',self)
        self.loginMsg = QMessageBox()
        self.setWindowTitle('Login')      
        self.login = LoginBL()
        self.username = ''
        self.password = ''
        #Button Events
        self.pushButton_login.clicked.connect(self.Login_Clicked)
        self.createAccount_commandLinkButton.clicked.connect(self.Signup_Clicked)

    def Login_Clicked(self):
        self.username = self.lineEdit_userName.text()
        self.password = self.lineEdit_password.text()
        
        #Checks if the username and password is valid
        if self.login.loginState(self.username, self.password):
            self.loginMsg.setText(self.login.checkAccount(self.username,self.password))
            self.loginMsg.exec_()  
            
            #Check if a user or an Admin
            if self.login.getAccountType(self.username) == "Admin":
                self.adminWindow = Admin.Admin()
                self.adminWindow.show()
                self.close()
            else:
                self.userWindow = User.User(self.username)
                self.userWindow.show()
                self.close()
        else:
            self.loginMsg.setText(self.login.checkAccount(self.username,self.password))
            self.loginMsg.exec_()    
            self.lineEdit_userName.setText('')
            self.lineEdit_password.setText('')
               
              
    def Signup_Clicked(self):       
        signUpWindow = signUp.Ui_SignUp()
        signUpWindow.exec_()

    
if __name__ == "__main__":
    import sys
    app = QApplication(sys.argv)
    widget = Ui_Login()
    widget.show()
    sys.exit(app.exec_())