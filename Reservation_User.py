# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'c:\users\1014j_000\desktop\reservation_user.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1120, 847)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(100, 80, 471, 261))
        self.gridLayoutWidget.setObjectName("gridLayoutWidget")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.gridLayoutWidget)
        self.gridLayout_3.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.calendarWidget = QtWidgets.QCalendarWidget(self.gridLayoutWidget)
        self.calendarWidget.setObjectName("calendarWidget")
        self.gridLayout_3.addWidget(self.calendarWidget, 0, 0, 1, 1)
        self.verticalLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(620, 100, 392, 241))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout()
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.label_4 = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.label_4.setObjectName("label_4")
        self.verticalLayout_3.addWidget(self.label_4)
        self.label = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.label.setObjectName("label")
        self.verticalLayout_3.addWidget(self.label)
        self.label_5 = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.label_5.setObjectName("label_5")
        self.verticalLayout_3.addWidget(self.label_5)
        self.label_2 = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.label_2.setObjectName("label_2")
        self.verticalLayout_3.addWidget(self.label_2)
        self.label_3 = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.label_3.setObjectName("label_3")
        self.verticalLayout_3.addWidget(self.label_3)
        self.horizontalLayout_2.addLayout(self.verticalLayout_3)
        self.verticalLayout_4 = QtWidgets.QVBoxLayout()
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.lineEdit = QtWidgets.QLineEdit(self.verticalLayoutWidget)
        self.lineEdit.setObjectName("lineEdit")
        self.verticalLayout_4.addWidget(self.lineEdit)
        self.comboBox_4 = QtWidgets.QComboBox(self.verticalLayoutWidget)
        self.comboBox_4.setObjectName("comboBox_4")
        self.comboBox_4.addItem("")
        self.comboBox_4.addItem("")
        self.comboBox_4.addItem("")
        self.comboBox_4.addItem("")
        self.comboBox_4.addItem("")
        self.comboBox_4.addItem("")
        self.verticalLayout_4.addWidget(self.comboBox_4)
        self.comboBox = QtWidgets.QComboBox(self.verticalLayoutWidget)
        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.verticalLayout_4.addWidget(self.comboBox)
        self.comboBox_5 = QtWidgets.QComboBox(self.verticalLayoutWidget)
        self.comboBox_5.setObjectName("comboBox_5")
        self.comboBox_5.addItem("")
        self.comboBox_5.addItem("")
        self.comboBox_5.addItem("")
        self.comboBox_5.addItem("")
        self.comboBox_5.addItem("")
        self.comboBox_5.addItem("")
        self.comboBox_5.addItem("")
        self.comboBox_5.addItem("")
        self.comboBox_5.addItem("")
        self.verticalLayout_4.addWidget(self.comboBox_5)
        self.comboBox_3 = QtWidgets.QComboBox(self.verticalLayoutWidget)
        self.comboBox_3.setObjectName("comboBox_3")
        self.comboBox_3.addItem("")
        self.comboBox_3.addItem("")
        self.comboBox_3.addItem("")
        self.comboBox_3.addItem("")
        self.comboBox_3.addItem("")
        self.comboBox_3.addItem("")
        self.comboBox_3.addItem("")
        self.comboBox_3.addItem("")
        self.comboBox_3.addItem("")
        self.verticalLayout_4.addWidget(self.comboBox_3)
        self.horizontalLayout_2.addLayout(self.verticalLayout_4)
        self.verticalLayout_5.addLayout(self.horizontalLayout_2)
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.pushButton_2 = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.pushButton_2.setObjectName("pushButton_2")
        self.horizontalLayout_4.addWidget(self.pushButton_2)
        self.verticalLayout_5.addLayout(self.horizontalLayout_4)
        self.pushButton_3 = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.pushButton_3.setObjectName("pushButton_3")
        self.verticalLayout_5.addWidget(self.pushButton_3)
        self.tableWidget_schedule = QtWidgets.QTableWidget(self.centralwidget)
        self.tableWidget_schedule.setGeometry(QtCore.QRect(100, 380, 911, 371))
        self.tableWidget_schedule.setObjectName("tableWidget_schedule")
        self.tableWidget_schedule.setColumnCount(6)
        self.tableWidget_schedule.setRowCount(9)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_schedule.setVerticalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_schedule.setVerticalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_schedule.setVerticalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_schedule.setVerticalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_schedule.setVerticalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_schedule.setVerticalHeaderItem(5, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_schedule.setVerticalHeaderItem(6, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_schedule.setVerticalHeaderItem(7, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_schedule.setVerticalHeaderItem(8, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_schedule.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_schedule.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_schedule.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_schedule.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_schedule.setHorizontalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_schedule.setHorizontalHeaderItem(5, item)
        self.verticalLayoutWidget_4 = QtWidgets.QWidget(self.centralwidget)
        self.verticalLayoutWidget_4.setGeometry(QtCore.QRect(100, 380, 160, 80))
        self.verticalLayoutWidget_4.setObjectName("verticalLayoutWidget_4")
        self.verticalLayout_6 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_4)
        self.verticalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label_4.setText(_translate("MainWindow", "Organization:"))
        self.label.setText(_translate("MainWindow", "Room: "))
        self.label_5.setText(_translate("MainWindow", "Nature of Activity:"))
        self.label_2.setText(_translate("MainWindow", "Time Start:"))
        self.label_3.setText(_translate("MainWindow", "Time End:"))
        self.comboBox_4.setItemText(0, _translate("MainWindow", "AVR1"))
        self.comboBox_4.setItemText(1, _translate("MainWindow", "AVR2"))
        self.comboBox_4.setItemText(2, _translate("MainWindow", "AVR3"))
        self.comboBox_4.setItemText(3, _translate("MainWindow", "Plenary Hall"))
        self.comboBox_4.setItemText(4, _translate("MainWindow", "Seminar Room"))
        self.comboBox_4.setItemText(5, _translate("MainWindow", "Gym"))
        self.comboBox.setItemText(0, _translate("MainWindow", "Seminar"))
        self.comboBox.setItemText(1, _translate("MainWindow", "Orientation"))
        self.comboBox.setItemText(2, _translate("MainWindow", "Meeting"))
        self.comboBox_5.setItemText(0, _translate("MainWindow", "7:30"))
        self.comboBox_5.setItemText(1, _translate("MainWindow", "9:00"))
        self.comboBox_5.setItemText(2, _translate("MainWindow", "10:30"))
        self.comboBox_5.setItemText(3, _translate("MainWindow", "12:00"))
        self.comboBox_5.setItemText(4, _translate("MainWindow", "13:30"))
        self.comboBox_5.setItemText(5, _translate("MainWindow", "15:00"))
        self.comboBox_5.setItemText(6, _translate("MainWindow", "16:30"))
        self.comboBox_5.setItemText(7, _translate("MainWindow", "18:00"))
        self.comboBox_5.setItemText(8, _translate("MainWindow", "19:30"))
        self.comboBox_3.setItemText(0, _translate("MainWindow", "9:00"))
        self.comboBox_3.setItemText(1, _translate("MainWindow", "10:30"))
        self.comboBox_3.setItemText(2, _translate("MainWindow", "12:00"))
        self.comboBox_3.setItemText(3, _translate("MainWindow", "13:30"))
        self.comboBox_3.setItemText(4, _translate("MainWindow", "15:00"))
        self.comboBox_3.setItemText(5, _translate("MainWindow", "16:30"))
        self.comboBox_3.setItemText(6, _translate("MainWindow", "18:00"))
        self.comboBox_3.setItemText(7, _translate("MainWindow", "19:30"))
        self.comboBox_3.setItemText(8, _translate("MainWindow", "21:00"))
        self.pushButton_2.setText(_translate("MainWindow", "Reserve"))
        self.pushButton_3.setText(_translate("MainWindow", "Generate Schedule"))
        item = self.tableWidget_schedule.verticalHeaderItem(1)
        item.setText(_translate("MainWindow", "7:30 - 9:00 AM"))
        item = self.tableWidget_schedule.verticalHeaderItem(2)
        item.setText(_translate("MainWindow", "9:00 - 10:30 AM"))
        item = self.tableWidget_schedule.verticalHeaderItem(3)
        item.setText(_translate("MainWindow", "10:30 - 12:00 NN"))
        item = self.tableWidget_schedule.verticalHeaderItem(4)
        item.setText(_translate("MainWindow", "12:00 - 1:30 PM"))
        item = self.tableWidget_schedule.verticalHeaderItem(5)
        item.setText(_translate("MainWindow", "1:30 - 3:00 PM"))
        item = self.tableWidget_schedule.verticalHeaderItem(6)
        item.setText(_translate("MainWindow", "3:00 - 4:30 PM"))
        item = self.tableWidget_schedule.verticalHeaderItem(7)
        item.setText(_translate("MainWindow", "4:30 - 6:00 PM"))
        item = self.tableWidget_schedule.verticalHeaderItem(8)
        item.setText(_translate("MainWindow", "7:30 - 9:00 PM"))
        item = self.tableWidget_schedule.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "Mon"))
        item = self.tableWidget_schedule.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "Tue"))
        item = self.tableWidget_schedule.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "Wed"))
        item = self.tableWidget_schedule.horizontalHeaderItem(3)
        item.setText(_translate("MainWindow", "Thu"))
        item = self.tableWidget_schedule.horizontalHeaderItem(4)
        item.setText(_translate("MainWindow", "Sat"))
        item = self.tableWidget_schedule.horizontalHeaderItem(5)
        item.setText(_translate("MainWindow", "Sun"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

