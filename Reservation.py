# -*- coding: utf-8 -*-
"""
Created on Tue Oct  2 19:56:58 2018

@author: jvgca
"""
from Reservation_Filehandling import Reservation_fileHandling

class Reservation:
    
    def __init__(self):
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
        
    def KeepReservation(self):
        #Stores attributes to database
        fh = Reservation_fileHandling()
        fh.LoadDatabase()
        fh.AddReservation(self.natureOfActivity,
                          self.organization,
                          self.room,
                          self.month,
                          self.day,
                          self.year,
                          self.timeIn,
                          self.timeOut)
        fh.CloseDatabase()
    
    
        
    
        