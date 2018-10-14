# -*- coding: utf-8 -*-

import sys
sys.path.append('../')
import unittest
from BusinessLogic.UserBL import UserBL

class TestUser(unittest.TestCase):
    
    def test_GetOrganization(self):
        self.user = UserBL()
        self.assertEqual(self.user.GetOrganization("daynefradejas@gmail.com"), "ICPEP.SE")
#        self.assertEqual(self.user.GetOrganization("vhgaba@mymail.mapua.edu.ph"), "Honor Society of Mapua (HSM)")
#        self.assertEqual(self.user.GetOrganization("vsfabesamis@mymail.mapua.edu.ph"), "Mapua Integrated Computer Organization (MICRO)")
#        self.assertEqual(self.user.GetOrganization("user"), "Junior Philippine Computer Society - Mapua University (JPCS - MIT)") 
#        self.assertEqual(self.user.GetOrganization("Admin"), "Junior Philippine Computer Society - Mapua University (JPCS - MIT)")       
#      
#    def test_GetAvailableTime(self):
#        self.user = UserBL()
#        self.assertEqual(self.user.GetAvailableTime("Gym", "2018-10-25"), 
#                         ['07:30-9:00', '09:00-10:30', '10:30-12:00', '12:00-13:30', '13:30-15:00', '16:30-18:00', '18:00-19:30', '19:30-21:00'])
#    def test_GetAvailableTimeStart(self):
#        self.user = UserBL()
#        self.assertEqual(self.user.GetAvailableTimeStart("Gym", "2018-10-25"),
#                         ['07:30', '09:00', '10:30', '12:00', '13:30', '16:30', '18:00', '19:30'])
#    def test_GetAvailableTimeEnd(self):
#        self.user = UserBL()
#        self.assertEqual(self.user.GetAvailableTimeEnd("Gym", "2018-10-25"), 
#                         ['09:00', '10:30', '12:00', '13:30', '15:00', '18:00', '19:30', '21:00'])

        
        
        
        
if __name__ == '__main__':
    unittest.main()
       
    
    