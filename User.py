# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Login.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost! 
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
        
        self.GenerateTimeIn()
        self.GenerateTimeOut()
            
    def Reserve_Clicked(self):
        print("DAYNE")
        
   # def ShowSchedule(self):
      #  date = self.calendarWidget.selectedDate()
      # print (date)
    
    def GenerateTimeIn(self):
        timeIn = []
        timeIn = self.rfh.ReservedTimeIn("Gym", "September", 30, 2018)
        for x in timeIn:
            if self.comboBox_timeStart.findText(x) != -1:
                self.comboBox_timeStart.removeItem(self.comboBox_timeStart.findText(x))
    def GenerateTimeOut(self, startCurrentIndex):
        currentIndex = self.comboBox_timeStart.currentIndex()
        print(startCurrentIndex)
        #nextIndex = currentIndex + 1
       # index = 0
        #while currentIndex > index:
           # self.comboBox_timeEnd.removeItem(index)
           # index = index + 1
        """
        #check if comboBox with nextIndex is equal to any variables in timeOut
        timeOut = []
        timeOut = self.rfh.ReservedTimeIn("Gym", "September", 30, 2018)
        for x in timeOut:
            if self.comboBox_timeOut.findText(x) != 1:
                self.comboBox_timeOut.removeItem(self.comboBox_timeStart.findText(x))
        """
        
if __name__ == "__main__":
    import sys
    app = QApplication(sys.argv)
    widget = User("acsabesamis@mymail.mapua.edu.ph")
    widget.show()
    sys.exit(app.exec_())

