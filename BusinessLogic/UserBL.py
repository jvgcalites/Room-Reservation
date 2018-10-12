
# -*- coding: utf-8 -*-
"""
Created on Tue Oct  2 17:31:33 2018

@author: Dayne Fradejas
"""
import sys
sys.path.append('../')
from DataAccess.FileHandling import FileHandling
from datetime import datetime
import calendar

class UserBL:
     def __init__(self):
         self.timeStart = ['7:30','9:00','10:30','12:00','13:30','15:00','16:30','18:00','19:30']
         self.timeEnd = ['9:00','10:30','12:00','13:30','15:00','16:30','18:00','19:30','21:00']
         self.timeArray = ['7:30-9:00','9:00-10:30','10:30-12:00','12:00-13:30','13:30-15:00',
                        '15:00-16:30','16:30-18:00','18:00-19:30','19:30-21:00']
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
     def GetReservedTime(self, room, day, month, year):
         timeTaken = []
         
         self.lfh.LoadDatabase()
         time = self.lfh.getReservedTime(room, day, month, year) #contains a list with the same room and date
         self.lfh.CloseDatabase()
         if not time:
             return timeTaken
         else:
             for x in range (len(time)):
                 timeTaken = timeTaken + self.getTimeTaken(time[x][6], time[x][7])
         return sorted(list(timeTaken))
         
     
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
    
    #Returns the date format e.g Monday, Tuesday, and etc.
     def getDayFormat(self,date):#format 2018-02-18 Year,month,day
         return calendar.day_name[(datetime.strptime(date, '%Y-%m-%d')).weekday()]
     
     def getTableColumn(self,day):
         if day == 'Monday':
             return 0
         elif day =='Tuesday':
             return 1
         elif day == 'Wednesday':
             return 2
         elif day == 'Thursday':
             return 3
         elif day == 'Friday':
             return 4
         elif day == 'Saturday':
             return 5
         elif day == 'Sunday':
             return 6
         else:
             print('fail')
         
      
             
     def KeepReservation(self):
        #Stores attributes to database
        self.lfh.LoadDatabase()
        self.lfh.AddReservation(self.natureOfActivity,
                          self.organization,
                          self.room,
                          self.month,
                          self.day,
                          self.year,
                          self.timeIn,
                          self.timeOut)
        self.lfh.CloseDatabase()
    
    #Gets the organization of the email
     def GetOrganization(self, email):
        self.lfh.LoadDatabase()
        organization = self.lfh.GetOrganizationDatabase(email)
        self.lfh.CloseDatabase
        return organization
    
     def GetYear(self, date):
        splitDate = []
        splitDate = date.split('-') #splitDate = [YYYY,MM,DD]
        year = splitDate[0]
        return int(year)
    
     def GetMonth(self, date):
        splitDate = []
        splitDate = date.split('-')
        month = splitDate[1]
        return month

     def GetDay(self, date):
        splitDate = []
        splitDate = date.split('-')
        day = splitDate[2]
        return int(day)   
    
     def returnToFirstColumn(self,dayOfWeek,day):
         if dayOfWeek == 'Monday':
             return day
         elif dayOfWeek =='Tuesday':
             day = day - 1
             return day
         elif dayOfWeek == 'Wednesday':
             day = day - 2
             return day
         elif dayOfWeek == 'Thursday':
             day = day - 3
             return day
         elif dayOfWeek == 'Friday':
             day = day - 4
             return day
         elif dayOfWeek == 'Saturday':
             day = day - 5
             return day
         elif dayOfWeek == 'Sunday':
             day = day - 6
             return day
         else:
             print('fail')
             
            
    
#Unit Test

afh = UserBL()
print(afh.getAvailableTime('AVR1',18,'July',2018))
#print(afh.getAvaiableTimeEnd('AVR1',18,'July',2018))
#print(afh.getAvailableTime('AVR1',18,'July',2018))

