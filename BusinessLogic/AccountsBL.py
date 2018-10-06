import sys
sys.path.append('../')
from DataAccess.FileHandling import FileHandling

class AccountsBL:
    def __init__(self):
        self.fh = FileHandling()
        self.counter = 0
    #Returns a list of data of user having a student number of given    
    def getDataByStudentNumber(self, studentNumber):
        studentNumber = studentNumber.replace(' ','')
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
        studentNumber = studentNumber.replace(' ','')
        data = self.fh.GetDetailsByStudentNumber(studentNumber)
        if not data:
            return False
        else:
            return True
        self.fh.CloseDatabase()
    #Returns the string if file exists
    def showStateOfStudentNumber(self, studentNumber):
        self.fh.LoadDatabase()
        state = self.studentNumberExists(studentNumber.replace(' ',''))
        if not state:
            if studentNumber == '':
                return 'Please input a student number'
            if len(studentNumber) < 10 or len(studentNumber) > 10:
                return 'Invalid Student number format'
            else:
                return 'Student number does not exist'
        self.fh.CloseDatabase()    
        
        
    def getPasswordByStudentNumber(self, studentNumber):
        self.fh.LoadDatabase()
        studentNumber = studentNumber.replace(' ','')
        return self.fh.getPasswordByUserID(self.fh.getUserIDByStudentNumber(studentNumber))       
        self.fh.CloseDatabase()
        
    def updateInfo(self, lastName,givenName,#middleName,emailAddress,password, organization,
                    studentNumber,email):
                    #contactNumber,userID):
        self.fh.LoadDatabase()
               
        state1 = state2 = False
        self.fh.LoadDatabase()
        data  = self.fh.GetDetailsByStudentNumber(studentNumber)
        _givenName = data[0][1]
        _lastName = data[0][0]
        _email = data[0][3]
        
        if lastName == _lastName and givenName == _givenName and email == _email:
            print("No Changes has been made")
        else:
            if self.fh.checkEmailExists(email) == '':
                state1 = True 
                     
            if self.fh.checkGivenNameExists(givenName) == '' and self.fh.checkLastNameExists(lastName) != '' :
                state2 = True              
            elif self.fh.checkGivenNameExists(givenName) != '' and self.fh.checkLastNameExists(lastName)== '':
                state2 = True
            
            
            if state1 == True and state2 == True:
                print ("success")
    #            self.fh.UpdateDatabase(lastName,givenName,middleName,emailAddress,password,
    #                       organization,studentNumber,contactNumber,userID) 
            else:
                if state1 == False:
                    return "Email is already taken"
                elif state1 == False and state2 == False:
                    return "Both Email and Name are already Existing"
                else:# state1 == True and state2 == False and state3 == True or state1 == True and state2 == True and state2 == False:
                    return "Name already exists"
     
        self.fh.CloseDatabase()
        
"""
ah = AccountsBL()
print(ah.updateInfo('Fradejas','Dayn','2015100896','daynefradejas@gmail.co'))       
"""