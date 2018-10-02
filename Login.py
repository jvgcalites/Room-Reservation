# -*- coding: utf-8 -*-

from PyQt5.QtWidgets import QApplication, QDialog, QMessageBox
from PyQt5.uic import loadUi
from User import User
import Login_Filehandling
import SignUp
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
                        #If account type is Admin, go to admin page, else go to user page
                        if self.lfh.AccountType(self.lineEdit_userName.text())=="Admin":
                            #INSERT HERE ADMIN PAGE
                            #user = Reservation_User()
                            #user.show()
                            #user.exec_()
                            self.close() #Closes Login Window
                        else:
                            #USER PAGE
                            user = User(self.lineEdit_userName.text())
                            user.show()
                            #user.exec_()
                            self.close() #Closes Login Window
                        self.lineEdit_userName.clear()
                        self.lineEdit_password.clear()
        else:
            print("Program Exits")         
            
        #Close Database
        self.lfh.CloseDatabase()   
                  
    def Signup_Clicked(self):
        #self.close() #Closes Login window
        signUpWindow = SignUp.SignUp()
        signUpWindow.exec_()
        
if __name__ == "__main__":
    import sys
    app = QApplication(sys.argv)
    widget = Login()
    widget.show()
    sys.exit(app.exec_())

