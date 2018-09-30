# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Login.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost! 

from PyQt5.QtWidgets import QApplication, QMessageBox, QMainWindow
from PyQt5.uic import loadUi

class User(QMainWindow):
    def __init__(self):
        super(User, self).__init__()
        loadUi('User.ui',self)
        self.loginMsg = QMessageBox()
        self.setWindowTitle('Room Reservation')
     
        #Button Events
        self.pushButton_Reserve.clicked.connect(self.Reserve_Clicked)

    def Reserve_Clicked(self):
        print("DAYNE")
    
if __name__ == "__main__":
    import sys
    app = QApplication(sys.argv)
    widget = User()
    widget.show()
    sys.exit(app.exec_())

