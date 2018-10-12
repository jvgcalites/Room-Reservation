# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Login.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost! 
import sys
sys.path.append('../')
from PyQt5.QtWidgets import QApplication, QMessageBox, QMainWindow, QTableWidget,QTableWidgetItem
from PyQt5 import QtCore, QtGui 
from PyQt5.uic import loadUi
from BusinessLogic.UserBL import UserBL

class User(QMainWindow):
    def __init__(self):
        super(User, self).__init__()
        loadUi('../UserInterface/User.ui', self)
        self.setWindowTitle('Room Reservation')
        self.loginMsg = QMessageBox()
        
        #When Date is Selected
        self.calendarWidget.clicked.connect(lambda: self.showReservation(User))
        self.pushButton_ShowReservation.clicked.connect(lambda: self.showReservation_Clicked())
        self.pushButton_Reserve.clicked.connect(lambda: self.reserve_Clicked())
        
####################################################################################################################
        
    def showDate(self,User):
        userBL = UserBL()
        date = self.calendarWidget.selectedDate().toString(QtCore.Qt.ISODate)
        dayOfWeek =userBL.getDayFormat(date)
        dayColumn = userBL.getTableColumn(dayOfWeek)
        self.tableWidget_schedule.setItem(1,dayColumn,QTableWidgetItem('*'))
        day = userBL.GetDay(date)
        print(userBL.returnToFirstColumn(dayOfWeek,day))
        
    def showReservation(self,User):
        userBL = UserBL()
        date = self.calendarWidget.selectedDate().toString(QtCore.Qt.ISODate)
        self.tableWidget_schedule.clearContents()
        
        room = self.comboBox_Room.currentText()
        dayOfWeek =userBL.getDayFormat(date)
        firstDay = userBL.returnToFirstColumn(dayOfWeek,userBL.GetDay(date))
        month = userBL.GetMonth(date)
        year = userBL.GetYear(date)
        day = firstDay
        
        self.weekSchedule = []
        for x in range(0,7):
            reserve = userBL.GetReservedTime(room, day, month, year)
            if reserve == []:
                reserve = [' ']
            self.weekSchedule.append(reserve)
            day += 1
        
        self.populateTable(self.weekSchedule)
        
        
    
    def populateTable(self,weekSchedule):  
        symbol = '****'
        dayColumn = 0
        for day in weekSchedule:
            duration = day
            if duration[0] ==' ':
                duration = []
            elif duration[0] == '7:30-9:00':
                row = 0
                for x in range(0,len(duration)):
                    self.tableWidget_schedule.setItem(row,dayColumn,QTableWidgetItem(symbol))
                    row = row + 1
            elif duration[0] =='9:00-10:30':
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
                print('in row 7')
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
            dayColumn += 1
                
    def UserPopulateTable(self,duration,dayColumn): 
        symbol = '---'
        if duration[0] == '7:30-9:00':
            row = 0
            for x in range(0,len(duration)):
                self.tableWidget_schedule.setItem(row,dayColumn,QTableWidgetItem(symbol))
                row = row + 1
        elif duration[0] =='9:00-10:30':
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
                
    def showReservation_Clicked(self):
        userBL = UserBL()
        date = self.calendarWidget.selectedDate().toString(QtCore.Qt.ISODate)
        duration = userBL.getTimeTaken(self.comboBox_timeStart.currentText(),self.comboBox_timeEnd.currentText())
        dayOfWeek =userBL.getDayFormat(date)
        print('day of week ' + dayOfWeek)
        dayColumn = userBL.getTableColumn(dayOfWeek)
        self.tableWidget_schedule.clearContents()
        self.populateTable(self.weekSchedule)
        self.UserPopulateTable(duration,dayColumn)
        
    def reserve_Clicked(self):
        print ("value")
        
        
    
####################################################################################################################        
        
        
    def KeepReservation(self):
        #Stores attributes to database
        self.lfh.LoadDatabase()
        self.lfh.AddReservation(self.natureOfActivity,
                          self.organization,
                          self.room,
                          self.month,
                          self.day,
                          self.year,
                          self.timeIn,
                          self.timeOut)
        self.lfh.CloseDatabase()
    
    #Gets the organization of the email
    def GetOrganization(self, email):
        self.lfh.LoadDatabase()
        organization = self.lfh.GetOrganizationDatabase(email)
        self.lfh.CloseDatabase
        return organization
    
    def GetYear(self, date):
        splitDate = []
        splitDate = date.split('-') #splitDate = [YYYY,MM,DD]
        year = splitDate[0]
        return int(year)
    
    def GetMonth(self, date):
        splitDate = []
        splitDate = date.split('-')
        month = splitDate[1]
        return month

    def GetDay(self, date):
        splitDate = []
        splitDate = date.split('-')
        day = splitDate[2]
        return int(day)
        
   
    
if __name__ == "__main__":
    app = QApplication(sys.argv)
    widget = User()
    widget.show()
    sys.exit(app.exec_())

