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
        #When Date is Selected, show reserved timeStart and timeEnd
        #self.calendarWidget.clicked.connect(lambda: self.ShowAvailableTime(Schedule))
        #Button Events
        self.pushButton_reserve.clicked.connect(lambda: self.Reserve_Clicked())
        self.pushButton_remove.clicked.connect(lambda: self.Remove_Clicked())
    
    def Remove_Clicked(self):
        chosenRoom = self.comboBox_room.currentText()
        chosenDate = self.calendarWidget.selectedDate().toString(QtCore.Qt.ISODate)
        chosenTimeStart = self.comboBox_timeStart.currentText()
        chosenTimeEnd = self.comboBox_timeEnd.currentText()
 
        if self.schedBL.SchedExists(chosenRoom, chosenDate, chosenTimeStart, chosenTimeEnd) == True:
            self.MessageBox("Schedule Removed", "Remove Schedule")
            self.schedBL.RemoveSchedule(chosenRoom, chosenDate, chosenTimeStart, chosenTimeEnd)
        else:
            self.MessageBox("Schedule Does Not Exists. Try Again", "Remove Schedule")
        
        #Creates message box    
    def MessageBox(self, message, windowTitle):
        msg = QMessageBox()
        msg.setText(message) #show passed message variable
        msg.setWindowTitle(windowTitle)
        msg.setStandardButtons(QMessageBox.Ok)
        msg.exec_()   
        

if __name__ == "__main__":
    app = QApplication(sys.argv)
    widget = Schedule()
    widget.show()
    sys.exit(app.exec_())

