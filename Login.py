# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Login.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
<<<<<<< HEAD
# WARNING! All changes made in this file will be lost! 

from PyQt5.QtWidgets import QApplication, QDialog, QMessageBox
from PyQt5.uic import loadUi
import Login_Filehandling
import signUp
class Login(QDialog):
=======
# WARNING! All changes made in this file will be lost!
from PyQt5.QtWidgets import QMessageBox
from PyQt5 import QtCore, QtGui, QtWidgets
import reservation_User
from Reservation_Admin import Ui_MainWindowAdmin
import signUp
import Login_Filehandling

class Ui_login_Form(object):
>>>>>>> origin/REYES
    
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
<<<<<<< HEAD
                        print(self.lfh.AccountType(self.lineEdit_userName.text()))
                        if self.lfh.AccountType(self.lineEdit_userName.text()) == "Admin":
                            MainWindow = QtWidgets.QMainWindow()
                            ui = Reservation_Admin.Ui_MainWindowAdmin()
                            ui.setup(MainWindow)
                            MainWindow.show()
                        else:
                            window = QtWidgets.QMainWindow()
                            ui = Ui_MainWindow()
                            ui.setup(window)
                            window.show()
=======
                        if self.lfh.AccountType(self.lineEdit_userName.text())=="Admin":
                            User = reservation_User.Reservation_User()
                            User.show()
                            User.exec_()
                        else:
                            User = reservation_User.Reservation_User()
                            User.show()
                            User.exec_()
>>>>>>> origin/REYES
                        self.lineEdit_userName.clear()
                        self.lineEdit_password.clear()
        else:
            print("Program Exits")         
            
        #Close Database
<<<<<<< HEAD
        self.lfh.CloseDatabase()                     
    def Signup_Clicked(self):
        #self.close() #Closes Login window
        signUpWindow = signUp.signUp()
        signUpWindow.exec_()
    
=======
        self.lfh.CloseDatabase()
                     
    def Signup_Clicked(self, login_Form):
        #Opens SignUp Dialog
        signUpWindow = signUp.signUp()
        signUpWindow.exec_()
        signUpWindow.exec_()
        
        
    def setupUi(self, login_Form):
        #######################################################################
        self.lfh = Login_Filehandling.Login_fileHandling()
        self.loginMsg = QMessageBox()
        self.loginMsg.setWindowTitle('Reservation')   
        #######################################################################
        login_Form.setObjectName("login_Form")
        login_Form.resize(487, 374)
        self.lineEdit_userName = QtWidgets.QLineEdit(login_Form)
        self.lineEdit_userName.setGeometry(QtCore.QRect(120, 110, 301, 31))
        font = QtGui.QFont()
        font.setFamily("Tahoma")
        font.setPointSize(10)
        self.lineEdit_userName.setFont(font)
        self.lineEdit_userName.setObjectName("lineEdit_userName")
        self.lineEdit_password = QtWidgets.QLineEdit(login_Form)
        self.lineEdit_password.setGeometry(QtCore.QRect(120, 160, 301, 31))
        font = QtGui.QFont()
        font.setFamily("Tahoma")
        font.setPointSize(10)
        self.lineEdit_password.setFont(font)
        self.lineEdit_password.setText("")
        self.lineEdit_password.setObjectName("lineEdit_password")
        self.lineEdit_password.setEchoMode(QtWidgets.QLineEdit.Password)
        self.pushButton_login = QtWidgets.QPushButton(login_Form)
        self.pushButton_login.setGeometry(QtCore.QRect(210, 210, 111, 41))
        font = QtGui.QFont()
        font.setFamily("Tahoma")
        font.setPointSize(10)
        self.pushButton_login.setFont(font)
        self.pushButton_login.setObjectName("pushButton_login")
        ###############################################################################
        self.pushButton_login.clicked.connect(lambda: self.Login_Clicked(login_Form))
        ################################################################################
        self.createAccount_commandLinkButton = QtWidgets.QCommandLinkButton(login_Form)
        self.createAccount_commandLinkButton.setGeometry(QtCore.QRect(310, 320, 171, 48))
        self.createAccount_commandLinkButton.setObjectName("createAccount_commandLinkButton")
        self.label_userName = QtWidgets.QLabel(login_Form)
        self.label_userName.setGeometry(QtCore.QRect(20, 110, 101, 31))
        ####################################################################################
        self.createAccount_commandLinkButton.clicked.connect(lambda: self.Signup_Clicked(login_Form))
        #####################################################################################
        font = QtGui.QFont()
        font.setFamily("Tahoma")
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.label_userName.setFont(font)
        self.label_userName.setObjectName("label_userName")
        self.label_password = QtWidgets.QLabel(login_Form)
        self.label_password.setGeometry(QtCore.QRect(20, 160, 101, 31))
        font = QtGui.QFont()
        font.setFamily("Tahoma")
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.label_password.setFont(font)
        self.label_password.setObjectName("label_password")
        self.label_state = QtWidgets.QLabel(login_Form)
        self.label_state.setGeometry(QtCore.QRect(140, 70, 251, 31))
        font = QtGui.QFont()
        font.setFamily("Tahoma")
        font.setPointSize(11)
        font.setBold(False)
        font.setWeight(50)
        self.label_state.setFont(font)
        self.label_state.setText("")
        self.label_state.setObjectName("label_state")

        self.retranslateUi(login_Form)
        QtCore.QMetaObject.connectSlotsByName(login_Form)

    def retranslateUi(self, login_Form):
        _translate = QtCore.QCoreApplication.translate
        login_Form.setWindowTitle(_translate("login_Form", "Reservation"))
        self.pushButton_login.setText(_translate("login_Form", "Login"))
        self.createAccount_commandLinkButton.setText(_translate("login_Form", "Create Account"))
        self.label_userName.setText(_translate("login_Form", "Username"))
        self.label_password.setText(_translate("login_Form", "Password"))


>>>>>>> origin/REYES
if __name__ == "__main__":
    import sys
    app = QApplication(sys.argv)
    widget = Login()
    widget.show()
    sys.exit(app.exec_())

