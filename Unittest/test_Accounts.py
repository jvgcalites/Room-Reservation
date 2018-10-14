# -*- coding: utf-8 -*-

import sys
sys.path.append('../')
import unittest
from BusinessLogic.AccountsBL import AccountsBL

class TestAccounts(unittest.TestCase):
    
    def test_GetDataByStudentNumber(self):
        acct = AccountsBL()
        self.assertEqual(acct.getDataByStudentNumber('2015104500'),[('Calites','John','Vincent','calites@gmail.com','BIOLOGIC','2955735735','2015104500','09051234567')] )

    def test_studentNumberExists(self):
        acct = AccountsBL()
        self.assertTrue(acct.studentNumberExists('2015104503'))
        self.assertTrue(acct.studentNumberExists('2015104500'))
        self.assertFalse(acct.studentNumberExists('2015104509'))
        
    def test_showStateOfStudentNumber(self):
        acct = AccountsBL()
        self.assertEqual(acct.showStateOfStudentNumber('20151040'),'Invalid Student number format')
        self.assertEqual(acct.showStateOfStudentNumber(''),'Please input a student number')
        
    def test_checkDataState(self):
        acct = AccountsBL()
        self.assertEqual(acct.removeAccount('6525734676'),"Student number erased successfully!")
        

        
if __name__ == '__main__':
    unittest.main()
       
    
    