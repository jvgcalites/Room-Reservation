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
    
    def test_checkAccount(self):
        self.login = LoginBL()
        userNameUi = ''
        passwordUi = ''
        self.assertEqual(self.login.checkAccount(userNameUi,passwordUi),'Please complete all fields!')
        
        

        
        
        
        
if __name__ == '__main__':
    unittest.main()
       
    
    