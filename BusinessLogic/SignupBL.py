# -*- coding: utf-8 -*-

import re
import sys
sys.path.append('../')
import numpy as np

from DataAccess.FileHandling import FileHandling

class SignupBL:
    
    def __init__ (self):
        self.lastName = ""
        self.givenName = ""
        self.middleName = ""
        self.userName = ""
        self.emailAddress = ""
        self.password = ""
        self.organization = ""
        self.studentNumber = ""
        self.contactNumber = ""
        self.userType = ""

    def Check_Password(self):
        #minimum of 8 characters in length
        #at least 1 character of uppercase, lowercase, and digit
        if (len(self.password) < 8):
            return False
        elif not re.search("[a-z]", self.password):
            return False
        elif not re.search("[0-9]", self.password):
            return False
        elif not re.search("[A-Z]", self.password):
            return False
        else:
            return True
            
    def Check_StudentNumber(self):
        #student number contains 10 digits
        if len(self.studentNumber) == 10 and self.studentNumber.isdigit():
            return True
        else:
            return False
        
    def IsComplete(self):
        # Check if fields are empty
        if self.lastName == "":
            x = False
        elif self.givenName == "":
            x = False
        elif self.middleName == "":
            x = False
        elif self.emailAddress == "":
            x = False
        elif self.contactNumber == "":
            x = False
        elif self.organization == "Select One":
            x = False
        elif self.userType == "":
            x = False
        elif self.userName == "":
            x = False
        else:
            x = True
        return x

    def StoreInfo(self):
        #Stores attributes to database
        fh = FileHandling()
        fh.LoadDatabase()
        fh.InsertAccount(self.lastName,
                         self.givenName,
                         self.middleName,
                         self.userName,
                         self.emailAddress,
                         self.password,
                         self.organization,
                         self.studentNumber,
                         self.contactNumber,
                         self.GenerateID(self.userType))
        fh.CloseDatabase()
    def redunduncyState(self, username, studentnumber, emailAddress):
        fh = FileHandling()
        fh.LoadDatabase()
        if fh.getPasswordByUserName(username) == '':
            return True
        elif fh.getEmail(emailAddress) == '':
            return True
        elif fh.GetDetailsByStudentNumber(studentnumber) =='':
            return True
        else:
            return False
        fh.CloseDatabase()
        
    def checkRedunduncy(self,username, emailAddress, givenName):
        fh = FileHandling()
        fh.LoadDatabase()
        if fh.getPasswordByUserName(username): 
            return 'Username already taken'
        elif fh.getEmail(emailAddress): 
            return 'Email Address already taken'
        elif fh.getGivenName(givenName): 
            return 'Name already exists'     
        else:
            return 'Saved Successfully'
        fh.CloseDatabase()
        
        # This function generates 10 random numbers 
        # If userType is admin, the sum of the 10 random numbers is 50
        # If userType is user, the sum of the 10 random numbers is 51
    def GenerateID(self, userType):
            #Identify if userType is admin or user
            if userType == "Admin":
                _sum = 50
            else:
                _sum = 51
            #Generates 10 random numbers
            n = 10
            rnd_id = 0
            while len(str(rnd_id)) != 10:
                rnd_array = np.random.multinomial(_sum, np.ones(n)/n, size = 1)[0]
                rnd_id = ''.join(str(x) for x in rnd_array)
            return rnd_id
