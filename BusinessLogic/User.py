# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Login.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost! 
import re
import sys
from PyQt5.QtWidgets import QApplication, QMessageBox, QMainWindow
from PyQt5 import QtCore
from PyQt5.uic import loadUi

class User(QMainWindow):
    def __init__(self):
        super(User, self).__init__()
        loadUi('../UserInterface/User.ui',self)
        self.setWindowTitle('Room Reservation')
        self.loginMsg = QMessageBox()
        
        #When Date is Selected
        self.calendarWidget.clicked.connect(self.showDate)
        
    def showDate(self):
        print(self.calendarWidget.selectedDate().toString(QtCore.Qt.ISODate))
    def reserve_Clicked(self):
        print("value")
        
   
    
if __name__ == "__main__":
    app = QApplication(sys.argv)
    widget = User()
    widget.show()
    sys.exit(app.exec_())

