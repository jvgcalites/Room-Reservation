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
    def AddReservation(self,natureOfActivity, org, room, month, day, year, timeIn, timeOut):
            with self.conn:
                ##############################Write to Reservation Table##########################################
                self.c.execute('INSERT INTO Reservation VALUES (?,?,?,?,?,?,?,?)',
                               (natureOfActivity,  org, room, month, day, year, timeIn, timeOut))
                ###########################################################################################
                return "File Successfully Written!"
    #Returns the organization         
    def GetOrganization(self, email):
        with self.conn:
            self.c.execute("SELECT * FROM User WHERE EmailAddress=:EmailAddress",
                           {'EmailAddress':email})
            return self.c.fetchone()[4]
        
    #Accepts room and month in string ; day and year in integer
    def ReservedTimeStart(self, room, month, day, year):
        timeIn = [] #list
        with self.conn:
            #Scan the table, if room, month, day and year matches, append the 6th column (TimeIn) to the list
            for row in self.c.execute("SELECT * FROM Reservation WHERE Room=? AND Month=? AND Day=? AND Year=?" , (room, month, day, year,)):
                timeIn.append(self.c.fetchone()[6])
        return timeIn
    
    def ReservedTimeEnd(self, room, month, day, year):
        timeOut = []
        with self.conn:
            for row in self.c.execute("SELECT * FROM Reservation WHERE Room=? AND Month=? AND Day=? AND Year=?" , (room, month, day, year,)):
                timeOut.append(self.c.fetchone()[7])
        return timeOut   

    
            

            
    #def CheckAvailability(self):
        #Checks if the room, month, day, year, and time is available
"""
if __name__ == '__main__': 
    fh = Reservation_fileHandling()
    fh.LoadDatabase()
    fh.AddReservation("Seminar", "Junior Philippine Computer Society - Mapua University (JPCS - MIT)", "AVR2", "September", 30, 2018, "7:30", "9:00")
    fh.AddReservation("Seminar", "Institute of Electronics Engineers of the Philippines - Mapua Univeristy Chapter (IECEP-MIT)", "AVR2", "September", 30, 2018, "9:00", "10:30")
    fh.AddReservation("Orientation", "Mapua Integrated Computer Organization (MICRO)", "Gym", "September", 30, 2018, "10:30", "12:00")
    fh.AddReservation("Orientation", "Philippine Institute of Civil Engineers (PICE)", "Gym", "September", 30, 2018, "13:30", "15:00")
    fh.AddReservation("Meeting", "American Concrete Institute (ACI)", "Gym", "September", 30, 2018, "7:30", "9:00")
    fh.CloseDatabase()
"""

"""
if __name__=='__main__':
    fh = Reservation_fileHandling()
    fh.LoadDatabase()
    timeIn = []
    timeOut = []
    timeIn = fh.ReservedTimeIn("Gym", "September", 30, 2018)
    timeOut = fh.ReservedTimeOut("Gym", "September", 30, 2018)
    print(timeIn)
    print(timeOut)
    fh.CloseDatabase()
    """
