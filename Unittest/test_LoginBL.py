# -*- coding: utf-8 -*-


import sys
sys.path.append('../')
import unittest
from BusinessLogic.LoginBL import LoginBL

class TestLogin(unittest.TestCase):
    
    def test_checkAccount(self):
        login = LoginBL()
        userNameUi = ''
        passwordUi = ''
        self.assertEqual(login.checkAccount(userNameUi,passwordUi),'Please complete all fields!')
        
    def test_checkAccount1(self):
        login = LoginBL()
        userNameUi = 'user123'
        passwordUi = 'User12345'
        self.assertEqual(login.checkAccount(userNameUi,passwordUi),'Login successful!')
        
    def test_checkAccount2(self):
        login = LoginBL()
        userNameUi = 'user123'
        passwordUi = 'User1234'
        self.assertEqual(login.checkAccount(userNameUi,passwordUi),'Invalid Password')
     
    def test_checkAccount3(self):
        login = LoginBL()
        userNameUi = 'user12'
        passwordUi = 'User1234'
        self.assertEqual(login.checkAccount(userNameUi,passwordUi),'Invalid credentials')
        
    def test_loginState(self):
        login = LoginBL()
        userNameUi = 'user12'
        passwordUi = 'User1234'
        self.assertFalse(login.loginState(userNameUi,passwordUi))
        
            
    def test_loginState1(self):
        login = LoginBL()
        userNameUi = 'user123'
        passwordUi = 'User12345'
        self.assertTrue(login.loginState(userNameUi,passwordUi))
        
    def test_loginState2(self):
        login = LoginBL()
        userNameUi = ''
        passwordUi = ''
        self.assertFalse(login.loginState(userNameUi,passwordUi))
        
    def test_getAccountType(self):
        login = LoginBL()
        userName = 'user123'
        self.assertEqual(login.getAccountType(userName),'User')  
        
    def test_getAccountType1(self):
        login = LoginBL()
        userName = 'admin'
        self.assertEqual(login.getAccountType(userName),'Admin')
        
    def test_getEmailByUserName(self):
        login = LoginBL()
        userName = 'admin'
        self.assertEqual(login.getEmailByUserName(userName),'jvgcalites@mymail.mapua.edu.ph')
        
    def test_getEmailByUserName1(self):
        login = LoginBL()
        userName = 'user123'
        self.assertEqual(login.getEmailByUserName(userName),'calites@gmail.com')
        
        

        
        
        
        
if __name__ == '__main__':
    unittest.main()
       
    
    