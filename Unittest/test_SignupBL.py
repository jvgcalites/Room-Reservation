# -*- coding: utf-8 -*-
"""
Created on Sun Oct 14 22:00:20 2018

@author: jvgca
"""

import sys
sys.path.append('../')
import unittest
from BusinessLogic.SignupBL import SignupBL

class TestSignup(unittest.TestCase):
    
    def test_CheckPassword(self):
        self.signup = SignupBL()
        self.signup.password = 'Mapua12345'
        self.assertEquals(self.signup.Check_Password(),True)

    def test_CheckStudentNumber(self):
        self.signup = SignupBL()
        self.signup.studentNumber = '2015104503'
        self.assertEqual(self.signup.Check_StudentNumber(), True)
        
    def test_IsComplete(self):
        self.signup = SignupBL()
        self.signup.lastName == 'Calites'
        self.signup.givenName == 'John'
        self.signup.emailAddress == 'jvg@gmail.com'
        self.signup.contactNumber == '09081547898'
        self.signup.organization == 'ICpEP.SE-Mapua'
        self.signup.userType == 'Admin'
        self.signup.userName == 'jvgcalites'
        self.assertEqual(self.signup.IsComplete(),False)
        
   
    def test_GenerateID(self):
        signup = SignupBL()
        self.assertNotEqual(signup.GenerateID('Admin'), '1234567890')
        


        
if __name__ == '__main__':
    unittest.main()