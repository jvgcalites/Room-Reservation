# -*- coding: utf-8 -*-

from Reservation_Filehandling import Reservation_fileHandling
from PyQt5.QtWidgets import QApplication, QMessageBox, QMainWindow
from PyQt5.uic import loadUi

class User(QMainWindow):
    def __init__(self, email):
        self.email = email
        super(User, self).__init__()
        loadUi('User.ui',self)        
        self.loginMsg = QMessageBox()
        self.setWindowTitle('Room Reservation')
        
        #Initialize Reservation Filhandling
        self.rfh = Reservation_fileHandling() 
        self.rfh.LoadDatabase() 
        #Set the text of lineEdit to organization using email 
        self.lineEdit_Organization.setText(self.rfh.GetOrganization(self.email))

        #Button Events
        self.pushButton_Reserve.clicked.connect(lambda: self.Reserve_Clicked())
            
    def Reserve_Clicked(self):
        print("DAYNE")
        
if __name__ == "__main__":
    import sys
    app = QApplication(sys.argv)
    widget = User("acsabesamis@mymail.mapua.edu.ph") #Still Testing
    widget.show()
    sys.exit(app.exec_())

