# -*- coding: utf-8 -*-
"""
Created on Fri Oct  5 14:29:56 2018

@author: Jetto
"""

import sys
sys.path.append('../')
import unittest
from BusinessLogic.LoginBL import LoginBL

class TestLogin(unittest.TestCase):
    
    def test_checkAccount_with_no_username_and_password(self):
        self.login = LoginBL()
        userNameUi = ''
        passwordUi = ''
        self.assertEqual(self.login.checkAccount(userNameUi,passwordUi),'Please complete all fields!')
        
    def test_checkAccount_with_no_password(self):
        self.login = LoginBL()
        userNameUi = 'daynefradejas@gmail.com'
        passwordUi = ''
        self.assertEquals(self.login.checkAccount(userNameUi,passwordUi),'Please complete all fields!')
        
    def test_checkAccount_with_no_username(self):
        self.login = LoginBL()
        userNameUi = ''
        passwordUi = 'dayne123'
        self.assertEquals(self.login.checkAccount(userNameUi,passwordUi),'Please complete all fields!')
        
    def test_checkAccount_with_valid_input(self):
        self.login = LoginBL()
        userNameUi = 'daynefradejas@gmail.com'
        passwordUi = 'dayne123'
        self.assertEquals(self.login.checkAccount(userNameUi,passwordUi),'Login successful!')
        
    def test_checkAccount_with_invalid_username(self):
        self.login = LoginBL()
        userNameUi = '1daynefradejas@gmail.com'
        passwordUi = 'dayne123'
        self.assertEquals(self.login.checkAccount(userNameUi,passwordUi),'Invalid credentials')
        
    def test_checkAccount_with_invalid_password(self):
        self.login = LoginBL()
        userNameUi = 'daynefradejas@gmail.com'
        passwordUi = 'dayne12'
        self.assertEquals(self.login.checkAccount(userNameUi,passwordUi),'Invalid Password')
        
    def test_loginState_with_invalid_input(self):
        self.login = LoginBL()
        userNameUi = 'daynefradejas@gmail.com'
        passwordUi = 'dayne12'
        self.assertEquals(self.login.loginState(userNameUi,passwordUi),False)
        
    def test_loginState_with_valid_input(self):
        self.login = LoginBL()
        userNameUi = 'daynefradejas@gmail.com'
        passwordUi = 'dayne123'
        self.assertEquals(self.login.loginState(userNameUi,passwordUi),True)
        
    def test_getAccountType_user(self):
        self.login = LoginBL()
        userName = 'daynefradejas@gmail.com'
        self.assertEquals(self.login.getAccountType(userName),'User')
        
    def test_getAccountType_admin(self):
        self.login = LoginBL()
        userName = 'Admin'
        self.assertEquals(self.login.getAccountType(userName),'Admin')
        
    def test_GenerateId_user(self):
        self.login = LoginBL()
        userType = 'User'
        _sum = 51
        self.assertEquals(self.login.GenerateID(userType),_sum)
        
    def test_GenerateId_admin(self):
        self.login = LoginBL()
        userType = 'Admin'
        _sum = 50
        userId = self.login.GenerateID(userType)
        
        self.assertEquals(self.sum_digits(userId),_sum)
        
    def sum_digits(n):
        r = 0
        while n:
            r, n = r + n % 10, n // 10
        return r
        
        

        
        
        
        
if __name__ == '__main__':
    unittest.main()
       
    
    