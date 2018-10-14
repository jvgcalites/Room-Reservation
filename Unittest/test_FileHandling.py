# -*- coding: utf-8 -*-
"""
Created on Fri Oct  5 15:26:23 2018

@author: Jetto
"""

import sys
sys.path.append('../')
import unittest
from DataAccess.FileHandling import FileHandling

class TestFileHandling(unittest.TestCase):
    
    def test_getPasswordByUserName_with_valid_input(self):
        userName = 'daynefradejas@gmail.com'
        obj = FileHandling()
        obj.LoadDatabase()
        self.assertEquals(obj.getPasswordByUserName(userName),'dayne123')
        
    def test_getPasswordByUserName_with_invalid_input(self):
        userName = ''
        obj = FileHandling()
        obj.LoadDatabase()
        self.assertEquals(obj.getPasswordByUserName(userName),'')
        
    def test_getUserId(self):
        userName = 'daynefradejas@gmail.com'
        obj = FileHandling()
        obj.LoadDatabase()
        self.assertEquals(obj.getUserId(userName),'3464757375')
        
    def test_InsertAccount(self):
        username = 'daynefradejas@gmail.com'
        lastName = 'Fradejas'
        givenName = 'Dayne'
        middleName = 'James'
        emailAddress = 'daynefradejas@gmail.com'
        password = 'd123'
        organization = 'HSM'
        studentNumber = '123456789'
        contactNumber = '123123123'
        userID = '123123123'
        obj = FileHandling()
        obj.LoadDatabase()
        self.assertEqual(obj.InsertAccount(lastName, givenName,middleName,username,emailAddress,password, organization,
                          studentNumber, contactNumber, userID),'File Successfully Written!')
        
        
    
    
    
if __name__ == '__main__':
    unittest.main()
        
    