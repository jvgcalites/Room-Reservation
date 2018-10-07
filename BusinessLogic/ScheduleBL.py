# -*- coding: utf-8 -*-

import sys
sys.path.append('../')
from DataAccess.FileHandling import FileHandling
from BusinessLogic.UserBL import UserBL

class ScheduleBL(UserBL):
    
     def RemoveSchedule(self, room, date, timeStart, timeEnd):
         
         day = self.GetDay(date)
         month = self.GetMonth(date)
         year = self.GetYear(date)

         self.lfh.LoadDatabase()
         self.lfh.RemoveSchedule(room, day, month, year, timeStart, timeEnd) 
         self.lfh.CloseDatabase()
         
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

         
         
         
         

    

afh = ScheduleBL()
