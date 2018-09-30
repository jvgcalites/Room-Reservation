# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'c:\users\1014j_000\desktop\reservation_user.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

import re    
import sys
from Signup_Filehandling import Signup_fileHandling
from userInfo import UserInfo
from PyQt5.QtWidgets import QApplication, QDialog, QMessageBox
from PyQt5.uic import loadUi

from PyQt5 import QtCore, QtGui, QtWidgets

class Reservation_User(QtWidgets.QMainWindow):
    def __init__(self):
        super(Reservation_User, self).__init__()
        loadUi('Reservation_User.ui', self)
        self.setWindowTitle('Room Reservation')
        #Button Event
        #self.pushButton_signUp.clicked.connect(self.signUp_done)


if __name__ == "__main__":
    #import sys
    #app = QtWidgets.QApplication(sys.argv)
    #MainWindow = QtWidgets.QMainWindow()
    #ui = Reservation_User()
    #ui.setupUi(MainWindow)
    #MainWindow.show()
    #sys.exit(app.exec_())
    app = QApplication(sys.argv)
    widget = Reservation_User()
    widget.show()
    sys.exit(app.exec_())
