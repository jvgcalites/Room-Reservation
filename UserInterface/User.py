# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Login.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost! 

import sys
sys.path.append('../')
<<<<<<< HEAD
from PyQt5.QtWidgets import QApplication, QMessageBox, QMainWindow, QTableWidget,QTableWidgetItem
from PyQt5 import QtCore, QtGui 
=======
from BusinessLogic.UserBL import UserBL
from PyQt5.QtWidgets import QApplication, QMessageBox, QMainWindow
from PyQt5 import QtCore
>>>>>>> master
from PyQt5.uic import loadUi
from BusinessLogic.UserBL import UserBL

class User(QMainWindow):
    def __init__(self, email):
        super(User, self).__init__()
        loadUi('../UserInterface/User.ui', self)
        self.setWindowTitle('Room Reservation')
        self.loginMsg = QMessageBox()
        #instantiate obj
        self.userBL = UserBL()
        #When Date is Selected
        self.calendarWidget.clicked.connect(lambda: self.showDate(User))
<<<<<<< HEAD
############################################################NOT FINAL########################################
    def showDate(self,User):
        userBL = UserBL()
        date = self.calendarWidget.selectedDate().toString(QtCore.Qt.ISODate)
        day =userBL.getDayFormat(date)
        print(date)
        print(day)
        column = userBL.getTableColumn(day)
        self.tableWidget_schedule.setItem(1,column,QTableWidgetItem('*'))

#############################################################################################################3
        
    def reserve_Clicked(self, User):
        print("value")
=======
        self.lineEdit_Organization.setText(self.userBL.GetOrganization(email))
        
        #Button Events
        self.pushButton_Reserve.clicked.connect(lambda: self.Reserve_Clicked())   
        
    def showDate(self,User):
        print(self.calendarWidget.selectedDate().toString(QtCore.Qt.ISODate))
               
    def Reserve_Clicked(self):
        self.ReservationInfo()
        self.userBL.KeepReservation()
        self.MessageBox("Schedule Reserved", "Success")
     
    def ReservationInfo(self):
        self.userBL.SetNatureOfActivity(self.comboBox_NatureOfActivity.currentText())
        self.userBL.SetOrganization(self.lineEdit_Organization.text())
        self.userBL.SetRoom(self.comboBox_Room.currentText())
        
        date = self.calendarWidget.selectedDate().toString(QtCore.Qt.ISODate) #date = "YYYY-MM-DD"
        self.userBL.SetMonth(self.userBL.GetMonth(date))
        self.userBL.SetDay(self.userBL.GetDay(date))
        self.userBL.SetYear(self.userBL.GetYear(date))
        
        self.userBL.SetTimeIn(self.comboBox_timeStart.currentText())
        self.userBL.SetTimeOut(self.comboBox_timeEnd.currentText())
        
    #Creates message box    
    def MessageBox(self, message, windowTitle):
        msg = QMessageBox()
        msg.setText(message) #show passed message variable
        msg.setWindowTitle(windowTitle)
        msg.setStandardButtons(QMessageBox.Ok)
        msg.exec_()        
>>>>>>> master
        
        
   
"""    
if __name__ == "__main__":
    app = QApplication(sys.argv)
    widget = User("user")
    widget.show()
    sys.exit(app.exec_())
"""
