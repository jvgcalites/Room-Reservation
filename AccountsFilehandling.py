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
        my_file = Path('Records.db')
        try:   #if database exists
            if not my_file.exists():
                raise ("Database does not exsist")
            else:
                self.conn = db.connect('Records.db')
                self.c = self.conn.cursor()
                return True
        except Exception as inst: #throw exception
            print (inst)            
            return False
    #Returns a value if the user is an Admin or a User
     def GetPasswordByEmail(self, email):
        with self.conn: #if there is a connection to the database
            self.c.execute("SELECT * FROM Login WHERE UserName=:UserName",{'UserName':email})
            if not self.c.fetchall(): #if no value is returned
                return -1
            else:
                self.c.execute("SELECT * FROM Login WHERE UserName=:UserName",{'UserName':email})
                return self.c.fetchone()[1]
     def CloseDatabase(self):
        self.conn.close()
