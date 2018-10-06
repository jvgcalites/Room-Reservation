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
        self.calendarWidget.clicked.connect(lambda: self.showDate(User))
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
        
        
   
    
if __name__ == "__main__":
    app = QApplication(sys.argv)
    widget = User()
    widget.show()
    sys.exit(app.exec_())

