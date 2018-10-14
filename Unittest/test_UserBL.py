# -*- coding: utf-8 -*-

import sys
sys.path.append('../')
import unittest
from BusinessLogic.UserBL import UserBL

class TestUser(unittest.TestCase):
    
    def test_GetOrganization(self):
        self.user = UserBL()
        self.assertEqual(self.user.GetOrganization("daynefradejas@gmail.com"), "ICPEP.SE")
        self.assertEqual(self.user.GetOrganization("vhgaba@mymail.mapua.edu.ph"), "Honor Society of Mapua (HSM)")
        self.assertEqual(self.user.GetOrganization("vsfabesamis@mymail.mapua.edu.ph"), "Mapua Integrated Computer Organization (MICRO)")
        self.assertEqual(self.user.GetOrganization("jvgcalites@mymail.mapua.edu.ph"), "PSM") 
        self.assertEqual(self.user.GetOrganization("calites@gmail.com"), "BIOLOGIC")       
      
    def test_GetAvailableTime(self):
        self.user = UserBL()
        self.assertEqual(self.user.GetAvailableTime("Seminar Room", "2018-10-25"), 
                         ['16:30-18:00', '18:00-19:30', '19:30-21:00'])
        
    def test_GetReserveTime(self):
        user = UserBL()
        self.assertEqual(user.GetReservedTime("Seminar Room",25, '10', 2018), 
                         ['07:30-09:00', '09:00-10:30', '10:30-12:00','12:00-13:30', '13:30-15:00','15:00-16:30'])
        
    def test_GetAvailableTimeStart(self):
        self.user = UserBL()
        self.assertEqual(self.user.GetAvailableTimeStart("Seminar Room", "2018-10-25"),
                         ['16:30', '18:00', '19:30'])
        
    def test_GetAvailableTimeEnd(self):
        self.user = UserBL()
        self.assertEqual(self.user.GetAvailableTimeEnd("Seminar Room", "2018-10-25"),['18:00', '19:30', '21:00'])
        
    def test_GetTimeTaken(self):
        user = UserBL()
        self.assertEqual(user.GetTimeTaken('07:30','12:00'), ['07:30-09:00','09:00-10:30','10:30-12:00'])
        
    def test_GetTimeStart(self):
        user = UserBL()
        self.assertEqual(user.GetTimeStart('07:30','12:00'), ['07:30','09:00','10:30'])
        
    def test_GetTimeEnd(self):
        user = UserBL()
        self.assertEqual(user.GetTimeEnd('07:30','12:00'),['09:00','10:30','12:00'])
        
    def test_GetDayFormat(self):
        user = UserBL()
        self.assertEqual(user.GetDayFormat('2018-10-25'),'Thursday')
        
    def test_GetDayFormat1(self):
        user = UserBL()
        self.assertNotEqual(user.GetDayFormat('2018-10-25'),'Friday')
        
    def test_GetDay(self):
        user = UserBL()
        self.assertEqual(user.GetDay('2018-10-25'), 25)
        
    def test_GetMonth(self):
        user = UserBL()
        self.assertEqual(user.GetMonth('2018-10-25'), '10')
        
    def test_GetYear(self):
        user = UserBL()
        self.assertEqual(user.GetYear('2018-10-25'), 2018)
        
    def test_SchedExists(self):
        user = UserBL()
        self.assertTrue(user.SchedExists("Seminar Room", "2018-10-25",'07:30','12:00'))
        
    def test_SchedExists1(self):
        user = UserBL()
        self.assertTrue(user.SchedExists("Seminar Room", "2018-10-25",'12:00','16:30'))    
        
    def test_SchedExists2(self):
        user = UserBL()
        self.assertFalse(user.SchedExists("Seminar Room", "2018-10-25",'16:30','21:00'))    
        
    def test_returnToFirstColumn(self):
        user = UserBL()
        self.assertEqual(user.returnToFirstColumn('Monday',7), 7)
        
    def test_returnToFirstColumn1(self):
        user = UserBL()
        self.assertEqual(user.returnToFirstColumn('Mondays',7), None)
        
    def test_getTableColumn(self):
        user = UserBL()
        self.assertEqual(user.getTableColumn('Monday'),0)
        
    def test_getTableColumn1(self):
        user = UserBL()
        self.assertEqual(user.getTableColumn('Sunday'),6)
              
    def test_getTableColumn2(self):
        user = UserBL()
        self.assertNotEqual(user.getTableColumn('Sunday'),7)
        
if __name__ == '__main__':
    unittest.main()
       
    
    