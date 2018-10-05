# -*- coding: utf-8 -*-

<<<<<<< HEAD:User.py
from Reservation_Filehandling import Reservation_fileHandling
from PyQt5.QtWidgets import QApplication, QMessageBox, QMainWindow
from PyQt5.uic import loadUi
from PyQt5 import QtCore
from Reservation import Reservation

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
        
    def GetYear(self):
        date = self.calendarWidget.selectedDate().toString(QtCore.Qt.ISODate) #date = "YYYY-MM-DD"
        splitDate = []
        splitDate = date.split('-') #splitDate = [YYYY,MM,DD]
        year = splitDate[0]
        return int(year)
    
    def GetMonth(self):
        date = self.calendarWidget.selectedDate().toString(QtCore.Qt.ISODate)
        splitDate = []
        splitDate = date.split('-')
        month = splitDate[1]
        return month

    def GetDay(self):
        date = self.calendarWidget.selectedDate().toString(QtCore.Qt.ISODate)
        splitDate = []
        splitDate = date.split('-')
        day = splitDate[2]
        return int(day)
               
    def Reserve_Clicked(self):
        self.newReservation = Reservation()
        self.ReservationInfo()
        
        self.newReservation.KeepReservation()
        self.MessageBox(self, "Schedule Reserved", "Success")
     
    def ReservationInfo(self):
        self.newReservation.SetNatureOfActivity(self.comboBox_NatureOfActivity.currentText())
        self.newReservation.SetOrganization(self.lineEdit_Organization.text())
        self.newReservation.SetRoom(self.comboBox_Room.currentText())
        self.newReservation.SetMonth(self.GetMonth())
        self.newReservation.SetDay(self.GetDay())
        self.newReservation.SetYear(self.GetYear())
        self.newReservation.SetTimeIn(self.comboBox_timeStart.currentText())
        self.newReservation.SetTimeOut(self.comboBox_timeEnd.currentText())
        
    #Creates message box    
    def MessageBox(self, message, windowTitle):
        msg = QMessageBox()
        msg.setText(message) #show passed message variable
        msg.setWindowTitle(windowTitle)
        msg.setStandardButtons(QMessageBox.Ok)
        msg.exec_()        
"""      
if __name__ == "__main__":
    import sys
    app = QApplication(sys.argv)
    widget = User("acsabesamis@mymail.mapua.edu.ph") #Still Testing
    widget.show()
    sys.exit(app.exec_())
"""
=======
# Form implementation generated from reading ui file 'Login.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost! 
import sys
from PyQt5.QtWidgets import QApplication, QMessageBox, QMainWindow
from PyQt5 import QtCore
from PyQt5.uic import loadUi

class User(QMainWindow):
    def __init__(self):
        super(User, self).__init__()
        loadUi('../UserInterface/User.ui', self)
        self.setWindowTitle('Room Reservation')
        self.loginMsg = QMessageBox()
        
        #When Date is Selected
        self.calendarWidget.clicked.connect(lambda: self.showDate(User))
        
    def showDate(self,User):
        print(self.calendarWidget.selectedDate().toString(QtCore.Qt.ISODate))
    def reserve_Clicked(self, User):
        print("value")
        
   
    
if __name__ == "__main__":
    app = QApplication(sys.argv)
    widget = User()
    widget.show()
    sys.exit(app.exec_())
>>>>>>> FRADEJAS:UserInterface/User.py

