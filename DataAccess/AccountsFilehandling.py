# -*- coding: utf-8 -*-
"""
Created on Tue Oct  2 17:31:33 2018

@author: Dayne Fradejas
"""

import sqlite3 as db
from pathlib import Path


class AccountsFileHandling:
     def __init__(self):
         self.conn = ''
         self.c = ''
    #Returns List of details through student number
     def GetDetailsByStudentNumber(self, studentNumber):
         with self.conn: #if there is a connection to the database
            self.c.execute("SELECT * FROM User WHERE StudentNumber=:StudentNumber",{'StudentNumber':studentNumber})
            if not self.c.fetchall(): #if no value is returned
                return -1
            else:
                self.c = self.conn.cursor()
                self.c.execute("SELECT * FROM User WHERE StudentNumber=:StudentNumber",{'StudentNumber':studentNumber}) 
                value = self.c.fetchall()
                return value
    #Load Database 
     def LoadDatabase(self):
        my_file = Path('../Database/Records.db')
        try:   #if database exists
            if not my_file.exists():
                raise ("Database does not exsist")
            else:
                self.conn = db.connect('../Database/Records.db')
                self.c = self.conn.cursor()
                return True
        except Exception as inst: #throw exception
            print (inst)            
            return False
        
    #Returns a value if the user is an Admin or a User
     def GetPasswordByUserName(self, userName):
        with self.conn: #if there is a connection to the database
            self.c.execute("SELECT * FROM Login WHERE UserName=:UserName",{'UserName':userName})
            if not self.c.fetchall(): #if no value is returned
                return ''
            else:
                self.c.execute("SELECT * FROM Login WHERE UserName=:UserName",{'UserName':userName})
                return self.c.fetchone()[1]
            
#     def EmailExists(self,email):
#         data = []
#         with self.conn:
#            self.c.execute("SELECT * FROM Login WHERE UserName=:UserName",{'UserName':email})
#            if not self.c.fetchall(): #if no value is returned
#                return data
#            else:
#                return False

     def UpdateDatabase(self, lastName,givenName,middleName,emailAddress,password,
                       organization,studentNumber,contactNumber,userID):
        with self.conn:
            self.c.execute('''UPDATE User SET 
                           LastName=:LastName,
                           GivenName=:GivenName,
                           MiddleName=:MiddleName,
                           EmailAddress=:EmailAddress, 
                           Organization=:Organization,
                           ContactNumber=:ContactNumber 
                           WHERE StudentNumber=:StudentNumber''',
                           {'LastName':lastName,
                            'GivenName':givenName, 
                            'MiddleName':middleName,
                            'EmailAddress':emailAddress,
                            'Organization':organization, 
                            'ContactNumber':contactNumber,
                            'StudentNumber':studentNumber})
            self.c.execute('''UPDATE Login SET
                           Password=:Password, UserName=:UserName
                           WHERE UserID=:UserID''',{
                           'Password':password,'UserName':emailAddress,'UserID':userID})

    
     def RemoveAccount(self, userID):
        with self.conn:
            #Remove from User table
            self.ahl.c.execute("DELETE from User WHERE UserID =: UserID",{'UserID':userID})
            #Remove from Login table
            self.ahl.c.execute("DELETE from Login WHERE USerID =: UserID",{'UserID':userID})
            
     def CloseDatabase(self):
         self.conn.close()
"""
ac = AccountsFileHandling()
ac.LoadDatabase()
print(ac.EmailExists('peafradejas@gmail.com'))
ac.LoadDatabase()
"""