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