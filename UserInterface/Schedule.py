# -*- coding: utf-8 -*-

import sys
sys.path.append('../')
from BusinessLogic.ScheduleBL import ScheduleBL
<<<<<<< HEAD
from PyQt5.QtWidgets import QApplication, QMessageBox, QMainWindow, QTableWidget,QTableWidgetItem
=======
from PyQt5.QtWidgets import QApplication, QMessageBox, QMainWindow
>>>>>>> FRADEJAS
from PyQt5 import QtCore
from PyQt5.uic import loadUi

class Schedule(QMainWindow):
    def __init__(self):
        super(Schedule, self).__init__()
        loadUi('../UserInterface/Schedule.ui', self)
        self.setWindowTitle('Manage Schedule')
        self.loginMsg = QMessageBox()
<<<<<<< HEAD
        #instantiate ScheduleBL obj
        self.schedBL = ScheduleBL()
        #When Date is Selected, show taken schedule in tableWidget_Schedule
        self.calendarWidget.clicked.connect(lambda: self.showReservation(Schedule))
        self.comboBox_Room.currentIndexChanged.connect(lambda: self.showReservation(Schedule))
        #Button Events
        #When Reserve Button is clicked
        self.pushButton_Reserve.clicked.connect(lambda: self.Reserve_Clicked())
        #When Remove Buttons is clicked
        self.pushButton_Remove.clicked.connect(lambda: self.Remove_Clicked())
        #When Show Reservation Button is clicked
        self.pushButton_ShowReservation.clicked.connect(lambda: self.showReservation_Clicked())
=======
        
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
        
        self.pushButton_manageAccounts.clicked.connect(self.ManageAccounts_Clicked)
        self.commandLinkButton_signOut.clicked.connect(self.Signout_Clicked)
     
    def Signout_Clicked (self):
        import Login
        self.log = Login.Ui_Login()
        self.log.show()
        self.close()
    def ManageAccounts_Clicked(self):
        import Accounts
        self.acc = Accounts.Accounts()
        self.acc.show()
        self.close()
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
>>>>>>> FRADEJAS
        
    # When Reserve Button is clicked, save to data base                
    def Reserve_Clicked(self):
        chosenDate = self.calendarWidget.selectedDate().toString(QtCore.Qt.ISODate)
<<<<<<< HEAD
        chosenRoom = self.comboBox_Room.currentText()
=======
        chosenRoom = self.comboBox_room.currentText()
>>>>>>> FRADEJAS
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
            
<<<<<<< HEAD
    #Save data taken from user to ScheduleBL class attributes    
    def ReservationInfo(self):
        self.schedBL.SetNatureOfActivity(self.comboBox_NatureOfActivity.currentText())
        self.schedBL.SetOrganization(self.lineEdit_Organization.text())
        self.schedBL.SetRoom(self.comboBox_Room.currentText())
=======
        
    #Save data taken from user to UserBL class attributes    
    def ReservationInfo(self):
        self.schedBL.SetNatureOfActivity(self.comboBox_natureOfActivity.currentText())
        self.schedBL.SetOrganization(self.lineEdit_organization.text())
        self.schedBL.SetRoom(self.comboBox_room.currentText())
>>>>>>> FRADEJAS
        date = self.calendarWidget.selectedDate().toString(QtCore.Qt.ISODate) #date = "YYYY-MM-DD"
        self.schedBL.SetMonth(self.schedBL.GetMonth(date))
        self.schedBL.SetDay(self.schedBL.GetDay(date))
        self.schedBL.SetYear(self.schedBL.GetYear(date))
        self.schedBL.SetTimeIn(self.comboBox_timeStart.currentText())
        self.schedBL.SetTimeOut(self.comboBox_timeEnd.currentText())
<<<<<<< HEAD

=======
        
>>>>>>> FRADEJAS
        #Creates message box    
    def MessageBox(self, message, windowTitle):
        msg = QMessageBox()
        msg.setText(message) #show passed message variable
        msg.setWindowTitle(windowTitle)
        msg.setStandardButtons(QMessageBox.Ok)
        msg.exec_()   
<<<<<<< HEAD
    
    #Shows the week schedule of selected date    
    def showReservation(self,User):
        date = self.calendarWidget.selectedDate().toString(QtCore.Qt.ISODate)
        self.tableWidget_schedule.clearContents()
        room = self.comboBox_Room.currentText()
        dayOfWeek =self.schedBL.GetDayFormat(date)
        firstDay = self.schedBL.returnToFirstColumn(dayOfWeek,self.schedBL.GetDay(date))
        month = self.schedBL.GetMonth(date)
        year = self.schedBL.GetYear(date)
        day = firstDay
        
        self.weekSchedule = []
        for x in range(0,7):
            reserve = self.schedBL.GetReservedTime(room, day, month, year)
            if reserve == []:
                reserve = [' ']
            self.weekSchedule.append(reserve)
            day += 1
        print(self.weekSchedule)
        self.showWeekSchedule(self.weekSchedule,'organization')
        
        
    #Iterates the column from the first day of the week
    def showWeekSchedule(self,weekSchedule,symbol):  
        dayColumn = 0
        for day in weekSchedule:
            duration = day
            if duration[0] ==' ':
                duration = []
            else:
                self.populateTable(duration,dayColumn,symbol)
            dayColumn += 1
            
    #Sets symbols on reserved time schedule              
    def populateTable(self,duration,dayColumn,symbol): 
        if duration[0] == '07:30-09:00':
            row = 0
            for x in range(0,len(duration)):
                self.tableWidget_schedule.setItem(row,dayColumn,QTableWidgetItem(symbol))
                row = row + 1
        elif duration[0] =='09:00-10:30':
            row = 1
            for x in range(0,len(duration)):
                self.tableWidget_schedule.setItem(row,dayColumn,QTableWidgetItem(symbol))
                row = row + 1
        elif duration[0] == '10:30-12:00':
            row = 2
            for x in range(0,len(duration)):
                self.tableWidget_schedule.setItem(row,dayColumn,QTableWidgetItem(symbol))
                row = row + 1
        elif duration[0] == '12:00-13:30':
            row = 3
            for x in range(0,len(duration)):
                self.tableWidget_schedule.setItem(row,dayColumn,QTableWidgetItem(symbol))
                row = row + 1
        elif duration[0] == '13:30-15:00':
            row = 4
            for x in range(0,len(duration)):
                self.tableWidget_schedule.setItem(row,dayColumn,QTableWidgetItem(symbol))
                row = row + 1
        elif duration[0] == '15:00-16:30':
            row = 5
            for x in range(0,len(duration)):
                self.tableWidget_schedule.setItem(row,dayColumn,QTableWidgetItem(symbol))
                row = row + 1
        elif duration[0] == '16:30-18:00':
            row = 6
            for x in range(0,len(duration)):
                self.tableWidget_schedule.setItem(row,dayColumn,QTableWidgetItem(symbol))
                row = row + 1
        elif duration[0] == '18:00-19:30':
            row = 7
            for x in range(0,len(duration)):
                self.tableWidget_schedule.setItem(row,dayColumn,QTableWidgetItem(symbol))
                row = row + 1
        elif duration[0] == '19:30-21:00':
            row = 8
            for x in range(0,len(duration)):
                self.tableWidget_schedule.setItem(row,dayColumn,QTableWidgetItem(symbol))
                row = row + 1
        else:
                return'Invalid Time input'
               
    #Show the selected schedule of the user            
    def showReservation_Clicked(self):
        date = self.calendarWidget.selectedDate().toString(QtCore.Qt.ISODate)
        duration = self.schedBL.GetTimeTaken(self.comboBox_timeStart.currentText(),self.comboBox_timeEnd.currentText())
        dayOfWeek =self.schedBL.GetDayFormat(date)
        print('day of week ' + dayOfWeek)
        dayColumn = self.schedBL.getTableColumn(dayOfWeek)
        self.tableWidget_schedule.clearContents()
        self.showWeekSchedule(self.weekSchedule,'******')
        self.populateTable(duration,dayColumn,'-------')
=======
>>>>>>> FRADEJAS
        
    ##########################FEATURES FOR ADMIN############################################
    def Remove_Clicked(self):
        #variables
<<<<<<< HEAD
        chosenRoom = self.comboBox_Room.currentText()
=======
        chosenRoom = self.comboBox_room.currentText()
>>>>>>> FRADEJAS
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

