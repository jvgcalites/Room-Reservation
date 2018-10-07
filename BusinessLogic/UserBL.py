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
         self.timeStart = ['07:30','09:00','10:30','12:00','13:30','15:00','16:30','18:00','19:30']
         self.timeEnd = ['09:00','10:30','12:00','13:30','15:00','16:30','18:00','19:30', '21:00']
         self.timeArray = ['07:30-9:00','09:00-10:30','10:30-12:00','12:00-13:30','13:30-15:00',
                        '15:00-16:30','16:30-18:00','18:00-19:30','19:30-21:00']
         self.lfh = FileHandling()
         self.natureOfActivity = ""
         self.organization = ""
         self.room = ""
         self.month = ""
         self.day = 0
         self.year = 0
         self.timeIn = "" 
         self.timeOut = ""
         

     def SetNatureOfActivity(self, natureOfActivity):
         self.natureOfActivity = natureOfActivity
        
     def SetOrganization(self, organization):
         self.organization = organization
        
     def SetRoom(self, room):
         self.room = room
        
     def SetMonth(self, month):
         self.month = month
        
     def SetDay(self, day):
         self.day = day
        
     def SetYear(self, year):
         self.year = year
        
     def SetTimeIn(self, time):
         self.timeIn = time
        
     def SetTimeOut(self, time):
         self.timeOut = time
        
     #this function returns the vacant time
     #Year-integer, Month-String,Day-intege)
     def GetAvailableTime(self, room, date):        
         timeTaken = []
         
         day = self.GetDay(date)
         month = self.GetMonth(date)
         year = self.GetYear(date)
         
         self.lfh.LoadDatabase()
         time = self.lfh.getReservedTime(room, day, month, year) 
         self.lfh.CloseDatabase()
         if not time:
             return timeTaken
         else:
             for x in range (0,len(time)):
                 timeTaken = timeTaken + self.GetTimeTaken(time[x][6], time[x][7])                
         return sorted(list(set(self.timeArray) - set(timeTaken)))
         
              
     def GetReservedTime(self, room, day, month, year):
         timeTaken = []
         self.lfh.LoadDatabase()
         time = self.lfh.getReservedTime(room,day,month,year)
         self.lfh.CloseDatabase()   
         
         if not time: #if contains nothing
             return timeTaken
         else:
             for x in range (len(time)):
                timeTaken = timeTaken + self.getTimeTaken([x][6], time[x][7])                  
             return timeTaken
         
     # Returns the available timeStart based on room and date
     def GetAvailableTimeStart(self, room, date):
        timeTaken = []
        
        day = self.GetDay(date)
        month = self.GetMonth(date)
        year = self.GetYear(date)
        
        self.lfh.LoadDatabase()
        time = self.lfh.getTimeStart(room,day,month,year)
        self.lfh.CloseDatabase()
        
        if not time: #if contains nothing, which means that no slots are reserved in that room and day, return all time
             return self.timeStart
        else:
             for x in range (len(time)):
                 timeTaken = timeTaken + self.GetTimeStart(time[x][6], time[x][7])          
             return sorted(list(set(self.timeStart)-set(timeTaken)))
         
     # Returns the available timeEnd based on room and date   
     def GetAvailableTimeEnd(self, room, date):
        timeTaken = []
        day = self.GetDay(date)
        month = self.GetMonth(date)
        year = self.GetYear(date)
        
        self.lfh.LoadDatabase()
        time = self.lfh.getTimeEnd(room, day, month, year) # takes all the rows with the same room and date
        print (time)
        self.lfh.CloseDatabase()
        if not time:
            return self.timeEnd 
        else:
            for x in range (len(time)): 
                timeTaken = timeTaken + self.GetTimeEnd(time[x][6], time[x][7]) 
            return sorted(list(set(self.timeEnd)-set(timeTaken)))
    
     #Returns the array of the time between time start and timeEnd
     def GetTimeTaken(self, timeStart, timeEnd):
        timeTaken = []
        for x in range(self.timeStart.index(timeStart), self.timeEnd.index(timeEnd)+1):
            timeTaken.append(self.timeStart[x]+'-'+self.timeEnd[x])
        return timeTaken
    #Returns the array of the time start between time start and timeEnd
     def GetTimeStart(self,timeStart,timeEnd):
        timeTaken = []
        for x in range(self.timeStart.index(timeStart), self.timeEnd.index(timeEnd)+1):
            timeTaken.append(self.timeStart[x])
        return timeTaken
    #Returns the array of the time end between time start and timeEnd
     def GetTimeEnd(self,timeStart,timeEnd):
        timeTaken = []
        for x in range(self.timeStart.index(timeStart), self.timeEnd.index(timeEnd)+1):
            timeTaken.append(self.timeEnd[x])
        return timeTaken

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
 
#Unit Test

afh = UserBL()

#print(afh.getAvailableTime('AVR1',18,'July',2018))
#print(afh.GetAvailableTimeEnd('Gym', "2018-10-25"))
print(afh.GetAvailableTime('Gym', "2018-10-25"))
#print(afh.GetAvailableTimeStart('Gym', "2018-10-25"))
#print(afh.timeStart)
#print(afh.GetTimeEnd('15:00', '16:30'))

#print(afh.GetReservedTime("Gym", 25, "10", 2018))
#print(afh.GetAvailableTime("Gym", 25, "10", 2018))
#print(afh.GetAvailableTimeStart("Gym", "2018-10-15"))
#print(afh.GetAvailableTimeEnd("Gym", "2018-10-15"))


     #Get the time interval reserved sample format timeArray
"""
     def GetReservedTime(self, room, day, month, year):
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
"""
