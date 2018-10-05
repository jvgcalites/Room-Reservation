# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Login.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost! 
<<<<<<< HEAD:Accounts.py

from PyQt5.QtWidgets import QApplication, QWidget, QMessageBox
from PyQt5.uic import loadUi
import AccountsFilehandling
=======
import sys
sys.path.append('../')
from DataAccess.AccountsFilehandling import AccountsFileHandling
from PyQt5.QtWidgets import QApplication, QWidget, QMessageBox
from PyQt5.uic import loadUi
>>>>>>> FRADEJAS:UserInterface/Accounts.py
class Accounts(QWidget):
    
    def __init__(self):
        super(Accounts, self).__init__()
<<<<<<< HEAD:Accounts.py
        loadUi('Accounts.ui',self)
        self.loginMsg = QMessageBox()
        self.setWindowTitle('Room Reservation')
        self.ahl = AccountsFilehandling.AccountsFileHandling()
=======
        loadUi('../UserInterface/Accounts.ui',self)
        self.loginMsg = QMessageBox()
        self.setWindowTitle('Room Reservation')
        self.ahl = AccountsFileHandling()
>>>>>>> FRADEJAS:UserInterface/Accounts.py
        #Button Events
        self.pushButton_SaveChanges.clicked.connect(self.SaveChanges_Clicked)
        self.pushButton_ActivateEditMode.clicked.connect(self.ActivateEditMode_Clicked)
        self.pushButton_Search.clicked.connect(self.Search_Clicked)
        self.pushButton_RemoveAccount.clicked.connect(self.RemoveAccount_Clicked)
        
        
    def SaveChanges_Clicked(self):
<<<<<<< HEAD:Accounts.py
        print('Save')
=======
        self.ahl.LoadDatabase()
        if self.ahl.EmailExists(self.lineEdit_EmailAddress.text())==True:
            self.ahl.UpdateDatabase(self.lineEdit_Surname.text(),
                                    self.lineEdit_GivenName.text(),
                                    self.lineEdit_MiddleName.text(),
                                    self.lineEdit_EmailAddress.text(),
                                    self.lineEdit_Password.text(),
                                    self.lineEdit_Organization.text(),
                                    self.lineEdit_StudentNumber.text(),
                                    self.lineEdit_ContactNumber.text(),
                                    self.lineEdit_UserID.text())
            self.loginMsg.setText("Updated Sucessfully!")
            self.loginMsg.exec_()
            self.DisableLineEdits(True)
            self.ClearLineEdit()
            self.lineEdit_StudentNumber.clear()
            self.pushButton_SaveChanges.setDisabled(True)
        else:
            self.loginMsg.setText("Email address already exists!")
            self.loginMsg.exec_()
        self.ahl.CloseDatabase()
        
    def RemoveAccount_Clicked(self):
        
        self.ahl.LoadDatabase()
        self.ahl.RemoveAccount(self.lineEdit_UserID.text())
        self.ahl.CloseDatabase()
        self.loginMsg.setText("Account Removed Sucessfully!")
        self.loginMsg.exec_()
>>>>>>> FRADEJAS:UserInterface/Accounts.py
    def ActivateEditMode_Clicked(self):
        self.pushButton_SaveChanges.setEnabled(True)      
        #Activate the Line Edit for corrections
        self.DisableLineEdits(False)
    def Search_Clicked(self):
        self.ahl.LoadDatabase()
        value = self.ahl.GetDetailsByStudentNumber(self.lineEdit_StudentNumber.text())
        if len(self.lineEdit_StudentNumber.text()) != 10:
<<<<<<< HEAD:Accounts.py
            self.loginMsg.setText("Student nubmer can't be less than 10 characters!")            
=======
            self.DisableLineEdits(True)
            self.pushButton_ActivateEditMode.setEnabled(False)
            self.pushButton_RemoveAccount.setEnabled(False)
            self.loginMsg.setText("Student number format error (10 characters)")            
>>>>>>> FRADEJAS:UserInterface/Accounts.py
            self.loginMsg.exec_()
            self.lineEdit_StudentNumber.clear()
            #Clear Content
            self.ClearLineEdit()
            #Disable Save Changes button
            self.pushButton_SaveChanges.setEnabled(False)
            #Disable Line Edit
            self.DisableLineEdits(True)
            ###################################################################
        elif value != -1:
<<<<<<< HEAD:Accounts.py
=======
            self.DisableLineEdits(True)
            self.pushButton_ActivateEditMode.setEnabled(True)
            self.pushButton_RemoveAccount.setEnabled(True)
>>>>>>> FRADEJAS:UserInterface/Accounts.py
            self.lineEdit_Surname.setText(value[0][0])
            self.lineEdit_GivenName.setText(value[0][1])
            self.lineEdit_MiddleName.setText(value[0][2])
            self.lineEdit_EmailAddress.setText(value[0][3])
            self.lineEdit_UserID.setText(value[0][5])
            self.lineEdit_ContactNumber.setText(value[0][7])
            self.lineEdit_Organization.setText(value[0][4])
            ###################################################################
            self.lineEdit_Password.setText(self.ahl.GetPasswordByEmail(value[0][3]))
<<<<<<< HEAD:Accounts.py
        else:
=======
        else:            
            self.pushButton_ActivateEditMode.setEnabled(False)
            self.pushButton_RemoveAccount.setEnabled(False)
>>>>>>> FRADEJAS:UserInterface/Accounts.py
            #Clear Content
            self.ClearLineEdit()
            ##################################################################
            self.pushButton_SaveChanges.setEnabled(False) #Disable button
            ###################################################################
            self.loginMsg.setText("Student number does not exist")
            self.loginMsg.exec_()
            self.lineEdit_StudentNumber.clear()
<<<<<<< HEAD:Accounts.py
=======
 
>>>>>>> FRADEJAS:UserInterface/Accounts.py

        self.ahl.CloseDatabase()
    #Disables line Edits 
    def DisableLineEdits(self, state):
        self.lineEdit_Surname.setDisabled(state)
        self.lineEdit_GivenName.setDisabled(state)
        self.lineEdit_MiddleName.setDisabled(state)
        self.lineEdit_EmailAddress.setDisabled(state)
        self.lineEdit_Password.setDisabled(state)
<<<<<<< HEAD:Accounts.py
        self.lineEdit_UserID.setDisabled(state)
=======
        self.lineEdit_UserID.setDisabled(True)
>>>>>>> FRADEJAS:UserInterface/Accounts.py
        self.lineEdit_ContactNumber.setDisabled(state)
        self.lineEdit_Organization.setDisabled(state)       
        
    def ClearLineEdit(self):
        self.lineEdit_Surname.clear()
        self.lineEdit_GivenName.clear()
        self.lineEdit_MiddleName.clear()
        self.lineEdit_EmailAddress.clear()
        self.lineEdit_UserID.clear()
        self.lineEdit_ContactNumber.clear()
        self.lineEdit_Organization.clear()
<<<<<<< HEAD:Accounts.py
        self.lineEdit_Password.clear()        
        
    def RemoveAccount_Clicked(self):
        print('Remove')
=======
        self.lineEdit_Password.clear()    
        
>>>>>>> FRADEJAS:UserInterface/Accounts.py
    
if __name__ == "__main__":
    import sys
    app = QApplication(sys.argv)
    widget = Accounts()
    widget.show()
    sys.exit(app.exec_())
<<<<<<< HEAD:Accounts.py
=======

>>>>>>> FRADEJAS:UserInterface/Accounts.py
