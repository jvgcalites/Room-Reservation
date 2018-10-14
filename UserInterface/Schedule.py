# -*- coding: utf-8 -*-

import sys
sys.path.append('../')
from BusinessLogic.ScheduleBL import ScheduleBL
from PyQt5.QtWidgets import QApplication, QMessageBox, QMainWindow
from PyQt5 import QtCore
from PyQt5.uic import loadUi

class Schedule(QMainWindow):
    def __init__(self):
        super(Schedule, self).__init__()
        loadUi('../UserInterface/Schedule.ui', self)
        self.setWindowTitle('Manage Schedule')
        self.loginMsg = QMessageBox()
        
        #instantiate userBL obj
        self.schedBL = ScheduleBL()
        #When Date is Selected, show available timeStart and timeEnd
        self.calendarWidget.clicked.connect(lambda: self.ShowAvailableTime(Schedule))
        #When room comboBox is changed, show available timeStart and timeEnd
        self.comboBox_room.currentIndexChanged.connect(lambda: self.ShowAvailableTime(Schedule))
        #Button Events
        #When Reserve Button is clicked
        self.pushButton_reserve.clicked.connect(lambda: self.Reserve_Clicked())
        #When Remove Buttons is clicked
        self.pushButton_remove.clicked.connect(lambda: self.Remove_Clicked())
            
    def ShowAvailableTime(self,Schedule):
        #Clears all contents of timeStart and timeEnd comboBox
        self.comboBox_timeStart.clear()
        self.comboBox_timeEnd.clear()
        
        #variables 
        chosenDate = self.calendarWidget.selectedDate().toString(QtCore.Qt.ISODate)
        chosenRoom = self.comboBox_room.currentText()

        #Show list of available timeStart in comboBox_timeStart
        availableTimeStart = self.schedBL.GetAvailableTimeStart(chosenRoom, chosenDate) # returns available timeStart from database
        for x in range(0, len(availableTimeStart)):
            self.comboBox_timeStart.addItem(availableTimeStart[x]) #place available timeStart in the timeStart comboBox
            
        #Show list of available time end in comboBox_timeEnd
        availableTimeEnd = self.schedBL.GetAvailableTimeEnd(chosenRoom, chosenDate) # returns available timeEnd from database
        for x in range(0, len(availableTimeEnd)):
            self.comboBox_timeEnd.addItem(availableTimeEnd[x]) #place available timeEnd in the timeEnd comboBox
        
    # When Reserve Button is clicked, save to data base                
    def Reserve_Clicked(self):
        chosenDate = self.calendarWidget.selectedDate().toString(QtCore.Qt.ISODate)
        chosenRoom = self.comboBox_room.currentText()
        chosenTimeStart = self.comboBox_timeStart.currentText()
        chosenTimeEnd = self.comboBox_timeEnd.currentText()
        #Scan the table if slot with room, date, timeStart, timeEnd already exists
        if self.schedBL.SchedExists(chosenRoom, chosenDate, chosenTimeStart, chosenTimeEnd) == False:
            #if schedule does not exists, you can reserve
            self.ReservationInfo()
            self.schedBL.KeepReservation()
            self.MessageBox("Schedule Reserved", "Success")
        else:
            #else you can't xD
            self.MessageBox("Schedule Already Exists. Please try Again", "Error")
            
        
        #Save data taken from user to UserBL class attributes    
    def ReservationInfo(self):
        self.schedBL.SetNatureOfActivity(self.comboBox_natureOfActivity.currentText())
        self.schedBL.SetOrganization(self.lineEdit_organization.text())
        self.schedBL.SetRoom(self.comboBox_room.currentText())
        date = self.calendarWidget.selectedDate().toString(QtCore.Qt.ISODate) #date = "YYYY-MM-DD"
        self.schedBL.SetMonth(self.schedBL.GetMonth(date))
        self.schedBL.SetDay(self.schedBL.GetDay(date))
        self.schedBL.SetYear(self.schedBL.GetYear(date))
        self.schedBL.SetTimeIn(self.comboBox_timeStart.currentText())
        self.schedBL.SetTimeOut(self.comboBox_timeEnd.currentText())
        
        #Creates message box    
    def MessageBox(self, message, windowTitle):
        msg = QMessageBox()
        msg.setText(message) #show passed message variable
        msg.setWindowTitle(windowTitle)
        msg.setStandardButtons(QMessageBox.Ok)
        msg.exec_()   
        
    ##########################FEATURES FOR ADMIN############################################
    def Remove_Clicked(self):
        #variables
        chosenRoom = self.comboBox_room.currentText()
        chosenDate = self.calendarWidget.selectedDate().toString(QtCore.Qt.ISODate)
        chosenTimeStart = self.comboBox_timeStart.currentText()
        chosenTimeEnd = self.comboBox_timeEnd.currentText()
        #if Schedule does exists, can remove
        if self.schedBL.SchedExists(chosenRoom, chosenDate, chosenTimeStart, chosenTimeEnd) == True:
            self.MessageBox("Schedule Removed", "Remove Schedule")
            self.schedBL.RemoveSchedule(chosenRoom, chosenDate, chosenTimeStart, chosenTimeEnd)
        else: #else, there's nothing to remove
            self.MessageBox("Schedule Does Not Exists. Try Again", "Remove Schedule")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    widget = Schedule()
    widget.show()
    sys.exit(app.exec_())

