# -*- coding: utf-8 -*-

import sys
sys.path.append('../')
from BusinessLogic.UserBL import UserBL

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
         
     #Returns true if schedule exists, false if does not exists  
     def SchedExists(self, room, date, timeStart, timeEnd):
         day = self.GetDay(date)
         month = self.GetMonth(date)
         year = self.GetYear(date)
         
         self.lfh.LoadDatabase()
         if self.lfh.SchedExists(room, day, month, year, timeStart, timeEnd) == True:
             self.lfh.CloseDatabase()
             return True
         elif self.lfh.SchedExists(room, day, month, year, timeStart, timeEnd) == False: 
             self.lfh.CloseDatabase()
             return False
         else:
             return None

         
         
         
         

    
#Sample Unit Test
afh = ScheduleBL()
if afh.SchedExists("Gym","2018-10-25","19:30","21:00") == True:
    print("YES")
else:
    print("NO")
