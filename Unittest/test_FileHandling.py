# -*- coding: utf-8 -*-


import sys
sys.path.append('../')
import unittest
from DataAccess.FileHandling import FileHandling

class TestFileHandling(unittest.TestCase):
    
    def test_getPasswordByUserName_with_valid_input(self):
        userName = 'daynefradejas@gmail.com'
        obj = FileHandling()
        obj.LoadDatabase()
        self.assertEqual(obj.getPasswordByUserName(userName),'dayne123')
        
    def test_getPasswordByUserName_with_invalid_input(self):
        userName = ''
        obj = FileHandling()
        obj.LoadDatabase()
        self.assertEqual(obj.getPasswordByUserName(userName),'')
        
    def test_getUserId(self):
        userName = 'daynefradejas@gmail.com'
        obj = FileHandling()
        obj.LoadDatabase()
        self.assertEqual(obj.getUserId(userName),'3464757375')
        
    def test_GetDetailsByStudentNumber(self):
        obj = FileHandling()
        obj.LoadDatabase()
        self.assertEqual(obj.GetDetailsByStudentNumber('2015104500'),[('Calites', 'John', 'Vincent', 'calites@gmail.com', 'BIOLOGIC', '2955735735', '2015104500', '09051234567')])
        
    def test_checkEmailExists(self):
        obj = FileHandling()
        obj.LoadDatabase()
        self.assertEqual(obj.checkEmailExists('calites@gmail.com'),[('Calites', 'John', 'Vincent', 'calites@gmail.com', 'BIOLOGIC', '2955735735', '2015104500', '09051234567')])
        
    def test_checkGivenNameExists(self):
        obj = FileHandling()
        obj.LoadDatabase()
        self.assertEqual(obj.checkGivenNameExists('John'),'John')
        
    def test_getPasswordByUserID(self):
        obj = FileHandling()
        obj.LoadDatabase()
        self.assertEqual(obj.getPasswordByUserID('2955735735'),'User12345')
        
    def test_getUserIDByStudentNumber(self):
        obj = FileHandling()
        obj.LoadDatabase()
        self.assertEqual(obj.getUserIDByStudentNumber('2015104500'),'2955735735')
    
    def test_getReservedTime(self):
        obj =FileHandling()
        obj.LoadDatabase()
        self.assertEqual(obj.getReservedTime('Seminar Room',25,'10',2018),[('Seminar', 'Junior Philippine Computer Society - Mapua University (JPCS - MIT)', 'Seminar Room', '10', 25, 2018, '07:30', '12:00'), ('Seminar', 'Junior Philippine Computer Society - Mapua University (JPCS - MIT)', 'Seminar Room', '10', 25, 2018, '12:00', '16:30')] )
    
    def test_getTimeStart(self):
        obj =FileHandling()
        obj.LoadDatabase()
        self.assertEqual(obj.getTimeStart('Seminar Room',25,'10',2018),[('Seminar', 'Junior Philippine Computer Society - Mapua University (JPCS - MIT)', 'Seminar Room', '10', 25, 2018, '07:30', '12:00'), ('Seminar', 'Junior Philippine Computer Society - Mapua University (JPCS - MIT)', 'Seminar Room', '10', 25, 2018, '12:00', '16:30')] )
    
    def test_getTimeEnd(self):
        obj =FileHandling()
        obj.LoadDatabase()
        self.assertEqual(obj.getTimeEnd('Seminar Room',25,'10',2018),[('Seminar', 'Junior Philippine Computer Society - Mapua University (JPCS - MIT)', 'Seminar Room', '10', 25, 2018, '07:30', '12:00'), ('Seminar', 'Junior Philippine Computer Society - Mapua University (JPCS - MIT)', 'Seminar Room', '10', 25, 2018, '12:00', '16:30')] )
    
    def test_GetOrganizationDatabase(self):
        obj = FileHandling()
        obj.LoadDatabase()
        self.assertEqual(obj.GetOrganizationDatabase('calites@gmail.com'), 'BIOLOGIC')
        
    def test_SchedAvailable(self):
        obj = FileHandling()
        obj.LoadDatabase()
        self.assertFalse(obj.SchedAvailable('Seminar Room', 25, '10', 2018))
        
    def test_SchedExists1(self):
        obj = FileHandling()
        obj.LoadDatabase()
        self.assertTrue(obj.SchedExists('Seminar Room', 25, '10', 2018,'07:30', '12:00'))
        
    def test_SchedExists2(self):
        obj = FileHandling()
        obj.LoadDatabase()
        self.assertFalse(obj.SchedExists('Seminar Room', 25, '10', 2018,'16:30', '21:00'))
    
    
if __name__ == '__main__':
    unittest.main()
        
    