# -*- coding: utf-8 -*-
"""
Created on Sun Sep 30 22:00:35 2018

@author: jvgca
"""
import sqlite3
from pathlib import Path

class Reservation_fileHandling:
    def __init__(self):
         self.conn = ''
         self.c = ''
    #Load Database 
    def LoadDatabase(self):
        my_file = Path('Records.db')
        try:   #if database exists
            if not my_file.exists():
                raise ("Database does not exsist")
            else:
                 self.conn = sqlite3.connect('Records.db')
                 self.c = self.conn.cursor()
        except Exception as inst: #throw exception
            print (inst)            
            
    def CloseDatabase(self):
        self.conn.close()
        
    #Returns a string if the writing of file is successfull or not
    def AddReservation(self,natureOfActivity, org, room, month, day, year, time):
            with self.conn:
                ##############################Write to Reservation Table##########################################
                self.c.execute('INSERT INTO Reservation VALUES (?,?,?,?,?,?,?)',
                               (natureOfActivity,  org, room, month, day, year, time))
                ###########################################################################################
                return "File Successfully Written!"
    #Returns the organization         
    def GetOrganization(self, email):
        with self.conn:
            self.c.execute("SELECT * FROM User WHERE EmailAddress=:EmailAddress",
                           {'EmailAddress':email})
            return self.c.fetchone()[4]
            
    #def CheckAvailability(self):
        #Checks if the room, month, day, year, and time is available
"""
if __name__ == '__main__': 
    fh = Reservation_fileHandling()
    fh.LoadDatabase()
    fh.AddReservation("Seminar", "HSM", "AVR1", "September", 30, 2018, "7:30-9:00")
    fh.CloseDatabase()
"""
