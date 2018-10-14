# -*- coding: utf-8 -*-

import sys
sys.path.append('../')
from BusinessLogic.UserBL import UserBL
import calendar
from datetime import datetime

class ScheduleBL(UserBL):
    
     #if room, date, timeStart, timeEnd matches, remove from database

    def RemoveSchedule(self, room, date, timeStart, timeEnd):

         #variables
         day = self.GetDay(date)
         month = self.GetMonth(date)
         year = self.GetYear(date)
         
         self.lfh.LoadDatabase()
         self.lfh.RemoveSchedule(room, day, month, year, timeStart, timeEnd) 
         self.lfh.CloseDatabase()
         
    #this function returns the vacant time
     #Year-integer, Month-String,Day-intege)
    def GetAvailableTime(self, room, date):        
         timeTaken = []
         
         day = self.GetDay(date)
         month = self.GetMonth(date)
         year = self.GetYear(date)
         
         self.lfh.LoadDatabase()
         time = self.lfh.getReservedTime(room, day, month, year) #contains a list with the same room and date
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
         time = self.lfh.getReservedTime(room, day, month, year) #contains a list with the same room and date
         self.lfh.CloseDatabase()
         if not time:
             return timeTaken
         else:
             for x in range (len(time)):
                 timeTaken = timeTaken + self.GetTimeTaken(time[x][6], time[x][7])
         return sorted(list(timeTaken))
     
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
         
    #Returns the date format e.g Monday, Tuesday, and etc.
    def GetDayFormat(self,date):#format 2018-02-18 Year,month,day
         return calendar.day_name[(datetime.strptime(date, '%Y-%m-%d')).weekday()]
     
    #Gets the organization of the email
    def GetOrganization(self, email):
        self.lfh.LoadDatabase()
        organization = self.lfh.GetOrganizationDatabase(email)
        self.lfh.CloseDatabase
        return organization
    
    #Returns year, input date [YYYY,MM,DD]
    def GetYear(self, date):
        splitDate = []
        splitDate = date.split('-') #splitDate = [YYYY,MM,DD]
        year = splitDate[0]
        return int(year)
    
    #Returns month, input date [YYYY,MM,DD]
    def GetMonth(self, date):
        splitDate = []
        splitDate = date.split('-')
        month = splitDate[1]
        return month

    #Returns day, inpput date [YYYY,MM,DD]
    def GetDay(self, date):
        splitDate = []
        splitDate = date.split('-')
        day = splitDate[2]
        return int(day)
         
    #Returns the first day of the week
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
    
    #Sets the column for the table widget         
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

         
         
         
         

    
#Sample Unit Test
afh = ScheduleBL()
if afh.SchedExists("Gym","2018-10-25","19:30","21:00") == True:
    print("YES")
else:
    print("NO")
