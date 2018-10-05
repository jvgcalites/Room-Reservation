import sys
sys.path.append('../')
from DataAccess.FileHandling import FileHandling

class AccountsBL:
    def __init__(self):
        self.fh = FileHandling()
    
    #Returns a list of data of user having a student number of given    
    def getDataByStudentNumber(self, studentNumber):
        self.fh.LoadDatabase()
        data = []
        state = self.studentNumberExists(studentNumber)
        if state:
            data = self.fh.GetDetailsByStudentNumber(studentNumber)
            return data
        else:
            return data
        self.fh.CloseDatabase()
    #Checks if Student Number Exists
    def studentNumberExists(self, studentNumber):
        self.fh.LoadDatabase()
        data = self.fh.GetDetailsByStudentNumber(studentNumber)
        if not data:
            return False
        else:
            return True
        self.fh.CloseDatabase()
    #Returns the string if file exists
    def showStateOfStudentNumber(self, studentNumber):
        self.fh.LoadDatabase()
        state = self.studentNumberExists(studentNumber)
        if not state:
            if len(studentNumber) < 10 or len(studentNumber) > 10:
                return 'Invalid Student number format'
            else:
                return 'Student number does not exist'
        self.fh.CloseDatabase()    
        

ac = AccountsBL()
print(ac.getDataByStudentNumber('2015100895')) 
