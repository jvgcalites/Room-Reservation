# -*- coding: utf-8 -*-
"""
Created on Sun Sep 23 12:36:06 2018

@author: jvgca
"""
import re
from Signup_Filehandling import Signup_fileHandling

class UserInfo:
    
    def __init__ (self):
        self.lastName = ""
        self.givenName = ""
        self.middleName = ""
        self.emailAddress = ""
        self.password = ""
        self.organization = ""
        self.studentNumber = ""
        self.contactNumber = ""
        self.userType = ""
    
    def SetLastName(self, lastName):
        self.lastName = lastName
    
    def SetGivenName(self, givenName):
        self.givenName = givenName
        
    def SetMiddleName(self, middleName):
        self.middleName = middleName
        
    def SetEmailAddress(self, emailAddress):
        self.emailAddress = emailAddress
        
    def SetPassword(self, password):
        self.password = password
        
    def SetOrganization(self, organization):
        self.organization = organization
        
    def SetStudentNumber(self, studentNumber):
        self.studentNumber = studentNumber
        
    def SetContactNumber(self, contactNumber):
        self.contactNumber = contactNumber
    
    def SetUserType(self, userType):
        self.userType = userType
    #Getters    
    def GetLastName(self):
        return self.lastName
    
    def GetGivenName(self):
        return self.givenName
        
    def GetMiddleName(self):
        return self.middleName
        
    def GetEmailAddress(self):
        return self.emailAddress
        
    def GetPassword(self):
        return self.password
        
    def GetOrganization(self):
        return self.organization
        
    def GetStudentNumber(self):
        return self.studentNumber
        
    def GetContactNumber(self):
        return self.contactNumber
    
    def GetUserType(self):
        return self.userType
        
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
        else:
            x = True
        return x

    def StoreInfo(self):
        
        fh = Signup_fileHandling()
        fh.LoadDatabase()
        fh.InsertAccount(self.lastName,
                         self.givenName,
                         self.middleName,
                         self.emailAddress,
                         self.password,
                         self.organization,
                         self.studentNumber,
                         self.contactNumber,
                         self.userType)
        fh.CloseDatabase()
    
    