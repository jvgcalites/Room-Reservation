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
        self.assertEquals(obj.getPasswordByUserName(userName),'dayne123')
        
    def test_getPasswordByUserName_with_invalid_input(self):
        userName = ''
        obj = FileHandling()
        self.assertEquals(obj.getPasswordByUserName(userName),'')
        
    def test_getUserId(self):
        userName = 'daynefradejas@gmail.com'
        obj = FileHandling()
        self.assertEquals(obj.getUserId(userName),'3464757375')
        
    def test_InsertAccount(self):
        username = 'daynefradejas@gmail.com'
        lastName = 'Fradejas'
        givenName = 'Dayne'
        middleName = ''
        emailAddress = 'daynefradejas@gmail.com'
        password = 'dayne123'
        organization = ''
        studentNumber = ''
        contactNumber = ''
        userType = 'admin'
        obj = FileHandling()
        self.assertEqual(obj.InsertAccount(lastName, givenName,middleName,username,emailAddress,password, organization,
                          studentNumber, contactNumber, userType),'File Successfully Written!')
        
    def test_GetDetailsByStudentNumber(self):
        obj = FileHandling()
        studentNumber = ' '
        self.assertEquals(obj.GetDetailsByStudentNumber(studentNumber),-1)
        
    def test_getEmail(self):
        obj = FileHandling()
        email = 'daynefradejas@gmail.com'
        self.assertEquals(obj.getEmail(email),'daynefradejas@gmail.com')
        
        
        
        
    
    
    
if __name__ == '__main__':
    unittest.main()
        
    