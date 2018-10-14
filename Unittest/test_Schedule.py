# -*- coding: utf-8 -*-

import sys
sys.path.append('../')
import unittest
from BusinessLogic.ScheduleBL import ScheduleBL

class TestSchedule(unittest.TestCase):
    
    def test_RemoveSchedule(self):
        self.sched = ScheduleBL()
        self.assertEqual(self.sched.RemoveSchedule('Gym', '2018-10-25', '18:00', '19:30'), None)
        
        
        
        
if __name__ == '__main__':
    unittest.main()
       
    
    