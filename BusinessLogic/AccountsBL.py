import sys
sys.path.append('../')
from DataAccess.FileHandling import FileHandling

class AccountsBL:
    def __init__(self):
        self.fh = FileHandling()
        self.lastName = ''
        self.givenName = ''
        self.middleName =''
        self.email=''
        self.password=''
        self.organization= ''
        self.studentNumber = ''
        self.contactNumber = ''
        self.userID =''
    
    def initializeVariables(self,lastName,givenName,middleName,email,password,
                       organization,studentNumber,contactNumber,userID):
        self.lastName = lastName
        self.givenName = givenName
        self.middleName = middleName
        self.email=email
        self.password=password
        self.organization= organization
        self.studentNumber = studentNumber
        self.contactNumber = contactNumber
        self.userID = userID
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
        state = self.studentNumberExists(studentNumber)
        if not state:
            if len(studentNumber) == 0:
                return 'Please input a student number'
            if len(studentNumber) != 10:
                return 'Invalid Student number format'
            else:
                return 'Student number does not exist'  
               
    def getPasswordByStudentNumber(self, studentNumber):
        self.fh.LoadDatabase()
        studentNumber = studentNumber.replace(' ','')
        return self.fh.getPasswordByUserID(self.fh.getUserIDByStudentNumber(studentNumber))       
        self.fh.CloseDatabase()
        
    def updateInfoStatus(self):         
        self.fh.LoadDatabase()
        state1 = state2 = False

        data  = self.fh.GetDetailsByStudentNumber(self.studentNumber)
        _givenName = data[0][1]
        _lastName = data[0][0]
        _email = data[0][3]
        
        if self.lastName == _lastName and self.givenName == _givenName and self.email == _email:
                self.fh.UpdateDatabase(self.lastName,self.givenName,self.middleName,self.email,self.password,
                           self.organization,self.studentNumber,self.contactNumber,self.userID) 
                return "Data has been updated!"
        else:    
            if _givenName != self.givenName and _lastName == self.lastName and self.email == _email:
                state1 = True 
            elif _givenName != self.givenName and _lastName != self.lastName and self.email == _email:
                state1 = True
            elif self.fh.checkEmailExists(self.email) == '':
                state1 = True                     
            
            #If given name doesn't exist
            if self.fh.checkGivenNameExists(self.givenName) == '' and self.fh.checkLastNameExists(self.lastName) != '' :
                state2 = True              
            elif self.fh.checkGivenNameExists(self.givenName) != '' and self.fh.checkLastNameExists(self.lastName) == '':
                state2 = True
            elif self.fh.checkGivenNameExists(self.givenName) == '' and self.fh.checkLastNameExists(self.lastName) == '':
                state2 = True

            if state1 == True and state2 == True:
               self.fh.UpdateDatabase(self.lastName,self.givenName,self.middleName,self.email,self.password,
                                      self.organization,self.studentNumber,self.contactNumber,self.userID) 
               return "Data has been updated!"
            else:
                if state1 == False:
                    return "Email is already taken"
                elif state1 == False and state2 == False:
                    return "Both Email and Name are already Existing"
                else:
                    return "Name already exists"
     
        self.fh.CloseDatabase()
    def checkDataState(self):
        
        self.fh.LoadDatabase()
        
        if self.updateInfoStatus() == 'Data has been updated!':
            return True
        else:
            return False
        
        self.fh.CloseDatabase()
    
    def removeAccount(self, userID):
        self.fh.LoadDatabase()       
        self.fh.RemoveAccount(userID)
        return "Student number erased successfully!"
        self.fh.CloseDatabase()
       
