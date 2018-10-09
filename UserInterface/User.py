# -*- coding: utf-8 -*-

import sys
sys.path.append('../')
from BusinessLogic.UserBL import UserBL
from PyQt5.QtWidgets import QApplication, QMessageBox, QMainWindow
from PyQt5 import QtCore
from PyQt5.uic import loadUi

class User(QMainWindow):
    def __init__(self, email):
        super(User, self).__init__()
        loadUi('../UserInterface/User.ui', self)
        self.setWindowTitle('Room Reservation')
        self.loginMsg = QMessageBox()
        
        #instantiate userBL obj
        self.userBL = UserBL()
        #Set text of user's organization in lineEdit automatically
        self.lineEdit_Organization.setText(self.userBL.GetOrganization(email))
        #When Date is Selected, show available timeStart and timeEnd
        self.calendarWidget.clicked.connect(lambda: self.ShowAvailableTime(User))
        #When room comboBox is changed, show available timeStart and timeEnd
        self.comboBox_Room.currentIndexChanged.connect(lambda: self.ShowAvailableTime(User))
        #Button Events
        self.pushButton_Reserve.clicked.connect(lambda: self.Reserve_Clicked())   
    
    #This function makes the comboBox for timeStart and timeEnd to automatically show the available slots     
    def ShowAvailableTime(self,User):
        #Clears all contents of timeStart and timeEnd comboBox
        self.comboBox_timeStart.clear()
        self.comboBox_timeEnd.clear()
        
        #variables 
        chosenDate = self.calendarWidget.selectedDate().toString(QtCore.Qt.ISODate)
        chosenRoom = self.comboBox_Room.currentText()

        #Show list of available timeStart in comboBox_timeStart
        availableTimeStart = self.userBL.GetAvailableTimeStart(chosenRoom, chosenDate)
        for x in range(0, len(availableTimeStart)):
            self.comboBox_timeStart.addItem(availableTimeStart[x]) 
            
        #Show list of available time end in comboBox_timeEnd
        availableTimeEnd = self.userBL.GetAvailableTimeEnd(chosenRoom, chosenDate)
        for x in range(0, len(availableTimeEnd)):
            self.comboBox_timeEnd.addItem(availableTimeEnd[x])
            
    # When Reserve Button is clicked, save to data base                
    def Reserve_Clicked(self):
        #variables
        chosenDate = self.calendarWidget.selectedDate().toString(QtCore.Qt.ISODate)
        chosenRoom = self.comboBox_Room.currentText()
        chosenTimeStart = self.comboBox_timeStart.currentText()
        chosenTimeEnd = self.comboBox_timeEnd.currentText()
        
        #Scan the table if slot with room, date, timeStart, timeEnd already exists
        if self.userBL.SchedExists(chosenRoom, chosenDate, chosenTimeStart, chosenTimeEnd) == False:
            #if schedule does not exists, you can reserve
            self.ReservationInfo()
            self.userBL.KeepReservation()
            self.MessageBox("Schedule Reserved", "Success")
        else:
            #else you can't xD
            self.MessageBox("Schedule Already Exists. Please try Again", "Error")
        
    #Save data taken from user to UserBL class attributes    
    def ReservationInfo(self):
        self.userBL.natureOfActivity = self.comboBox_NatureOfActivity.currentText()
        self.userBL.organization = self.lineEdit_Organization.text()
        self.userBL.room = self.comboBox_Room.currentText()
        date = self.calendarWidget.selectedDate().toString(QtCore.Qt.ISODate) #date = "YYYY-MM-DD"
        self.userBL.month = self.userBL.GetMonth(date)
        self.userBL.day = self.userBL.GetDay(date)
        self.userBL.year = self.userBL.GetYear(date)
        self.userBL.timeIn = self.comboBox_timeStart.currentText()
        self.userBL.timeOut = self.comboBox_timeEnd.currentText()
        
    #Creates message box    
    def MessageBox(self, message, windowTitle):
        msg = QMessageBox()
        msg.setText(message) #show passed message variable
        msg.setWindowTitle(windowTitle)
        msg.setStandardButtons(QMessageBox.Ok)
        msg.exec_()           

if __name__ == "__main__":
    app = QApplication(sys.argv)
    widget = User("user")
    widget.show()
    sys.exit(app.exec_())

