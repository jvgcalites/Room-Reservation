# -*- coding: utf-8 -*-
"""
Created on Tue Oct  2 17:31:33 2018

@author: Dayne Fradejas
"""

import sqlite3 as db
from pathlib import Path
from datetime import datetime
import calendar


class AccountsFileHandling:
     def __init__(self):
         self.conn = ''
         self.c = ''
         self.natureOfActivity = ['Seminar','Orientation','Meeting']
         self.room = ['Select item','AVR1','AVR2','AVR3','Plenary Hall','Seminar Room', 'Gym']
         self.timeStart = ['7:30','9:00','10:30','12:00','13:30','15:00','16:30','18:00','19:30']
         self.timeEnd = ['9:00','10:30','12:00','13:30','15:00','16:30','18:00','19:30']
         self.timeArray = ['7:30-9:00','9:00-10:30','10:30-12:00','12:00-13:30','13:30-15:00',
                        '15:00-16:30','16:30-18:00','18:00-19:30','19:30-21:30']
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
        
     #this function returns the vacant time
     #Year-integer, Month-String,Day-intege)
     def getAvailableTime(self, room, day, month, year):
        with self.conn: #if there is a connection to the database
            self.c.execute("SELECT * FROM Reservation WHERE Room = :Room AND Month = :Month AND Year =:Year AND Day= :Day ",
                           {'Room':room, 'Month':month,'Day':day,'Year':year})
            time = self.getReservedTime(year,day, month, year) 
            return sorted(list(set(self.timeArray) - set(time)))
        
     def getReservedTime(self, room, day, month, year):
        with self.conn: #if there is a connection to the database

            timeTaken = []
            self.c.execute("SELECT * FROM Reservation WHERE Room = :Room AND Month = :Month AND Year =:Year AND Day= :Day ",
                           {'Room':room, 'Month':month,'Day':day,'Year':year})
            time = self.c.fetchall()
            for x in range (len(time)):
                timeTaken.append(time[x][6]+'-'+time[x][7])                
            return timeTaken
        
     #returns the list of avaiable timeStart  
     def getAvailableTimeStart(self, room, day, month, year):
        timeTaken = []
        self.c.execute("SELECT * FROM Reservation WHERE Room = :Room AND Month = :Month AND Year =:Year AND Day= :Day ",
                           {'Room':room, 'Month':month,'Day':day,'Year':year})
        time = self.c.fetchall()
        for x in range (len(time)):
            timeTaken.append(time[x][6])   
        return sorted(list(set(self.timeStart)-set(timeTaken)))
      
     #returns the list of available timeEnd  
     def getAvaiableTimeEnd(self, room, day, month, year):
        timeTaken = []
        self.c.execute("SELECT * FROM Reservation WHERE Room = :Room AND Month = :Month AND Year =:Year AND Day= :Day ",
                           {'Room':room, 'Month':month,'Day':day,'Year':year})
        time = self.c.fetchall()
        for x in range (len(time)):
            timeTaken.append(time[x][7])   
        return sorted(list(set(self.timeEnd)-set(timeTaken)))
    
     #Returns the date format e.g Monday, Tuesday, and etc.
     def getDayFormat(self,date):#format 2018-02-18 Year,month,day
         return calendar.day_name[(datetime.strptime(date, '%Y-%m-%d')).weekday()]
         
     def CloseDatabase(self):
        self.conn.close()
#Unit Test
"""
afh = AccountsFileHandling()
afh.LoadDatabase()
print(afh.getAvailableTimeStart('AVR1',18,'July',2018))
print(afh.getAvaiableTimeEnd('AVR1',18,'July',2018))
afh.CloseDatabase()


afh = AccountsFileHandling()
afh.LoadDatabase()
print(afh.getDayFormat('2018-10-3'))
afh.CloseDatabase()
"""