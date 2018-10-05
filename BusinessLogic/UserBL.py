# -*- coding: utf-8 -*-
"""
Created on Tue Oct  2 17:31:33 2018

@author: Dayne Fradejas
"""
import sys
sys.path.append('../')
from DataAccess.FileHandling import FileHandling

class UserBL:
     def __init__(self):
         self.timeStart = ['7:30','9:00','10:30','12:00','13:30','15:00','16:30','18:00','19:30']
         self.timeEnd = ['9:00','10:30','12:00','13:30','15:00','16:30','18:00','19:30']
         self.timeArray = ['7:30-9:00','9:00-10:30','10:30-12:00','12:00-13:30','13:30-15:00',
                        '15:00-16:30','16:30-18:00','18:00-19:30','19:30-21:30']
         self.lfh = FileHandling()

     #this function returns the vacant time
     #Year-integer, Month-String,Day-intege)
     def getAvailableTime(self, room, day, month, year):        
         timeTaken = []
         self.lfh.LoadDatabase()
         time = self.lfh.getReservedTime(room, day,month,year)
         self.lfh.CloseDatabase()
         if not time:
             return timeTaken
         else:
             for x in range (0,len(time)):
                 timeTaken = timeTaken + self.getTimeTaken(time[x][6], time[x][7])                
         return sorted(list(set(self.timeArray) - set(timeTaken)))
         
         
     #Get the time interval reserved sample format timeArray
     def getReservedTime(self, room, day, month, year):
         timeTaken = []
         self.lfh.LoadDatabase()
         time = self.lfh.getReservedTime(room,day,month,year)
         self.lfh.CloseDatabase()   
         
         if not time: #if contains nothing
             return timeTaken
         else:
             for x in range (len(time)):
                 self.getAvailableTime([x][6], time[x][7])                  
             return timeTaken
     
     # Returns the available time start   
     def getAvailableTimeStart(self, room, day, month, year):
        timeTaken = []
        self.lfh.LoadDatabase()
        time = self.lfh.getTimeStart(room,day,month,year)
        self.getTimeStart()
        self.lfh.CloseDatabase()
        
        if not time: #if contains nothing
             return timeTaken
        else:
             for x in range (len(time)):
                 timeTaken = timeTaken + self.getTimeStart([x][6], time[x][7])          
             return sorted(list(set(self.timeStart)-set(timeTaken)))
        
     def getAvaiableTimeEnd(self, room, day, month, year):
        timeTaken = []
        self.lfh.LoadDatabase()

        time = self.lfh.getTimeEnd(room, day, month, year)
        self.lfh.CloseDatabase()
        if not time:
            return timeTaken 
        else:
            for x in range (len(time)):
                timeTaken = timeTaken + self.getTimeEnd(time[x][6], time[x][7]) 
                return sorted(list(set(self.timeEnd)-set(timeTaken)))
    
     #Returns the array of the time between time start and timeEnd
     def getTimeTaken(self, timeStart, timeEnd):
        timeTaken = []
        for x in range(self.timeStart.index(timeStart), self.timeEnd.index(timeEnd)+1):
            timeTaken.append(self.timeStart[x]+'-'+self.timeEnd[x])
        return timeTaken
    #Returns the array of the time start between time start and timeEnd
     def getTimeStart(self,timeStart,timeEnd):
        timeTaken = []
        for x in range(self.timeStart.index(timeStart), self.timeEnd.index(timeEnd)+1):
            timeTaken.append(self.timeStart[x])
        return timeTaken
    #Returns the array of the time end between time start and timeEnd
     def getTimeEnd(self,timeStart,timeEnd):
        timeTaken = []
        for x in range(self.timeStart.index(timeStart), self.timeEnd.index(timeEnd)+1):
            timeTaken.append(self.timeEnd[x])
        return timeTaken
            
    
#Unit Test

afh = UserBL()
print(afh.getAvailableTime('AVR1',18,'July',2018))
#print(afh.getAvaiableTimeEnd('AVR1',18,'July',2018))
#print(afh.getAvailableTime('AVR1',18,'July',2018))

