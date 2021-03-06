
#Author Dayne Fradejas
import sys
sys.path.append('../')
from DataAccess.FileHandling import FileHandling
import numpy as np

class LoginBL:
    def __init__(self):
        self.userName = ''
        self.password = ''
        self.lfh = FileHandling()
    
    #return if account is valid tpye Bool
    def checkAccount(self, userNameUi, passwordUi):
        self.lfh.LoadDatabase()
        if userNameUi == '' or passwordUi =='':
            return 'Please complete all fields!'
        elif self.lfh.getPasswordByUserName(userNameUi) == '':
            return 'Invalid credentials'
        elif self.lfh.getPasswordByUserName(userNameUi) == passwordUi:
            return 'Login successful!'
        else:
            return 'Invalid Password'
        self.lfh.CloseDatabase()
        
    def loginState(self, userNameUi, passwordUi):
        self.lfh.LoadDatabase()
        if self.lfh.getPasswordByUserName(userNameUi) == '':
            return False
        elif self.lfh.getPasswordByUserName(userNameUi) == passwordUi:
            return True
        else:
            return False   
        self.lfh.CloseDatabase()
    #return if the account is a user or an admin    
    def getAccountType(self, userName):
        self.lfh.LoadDatabase()
        userID = self.lfh.getUserId(userName)
        _sum = sum(map(int,userID))
        if _sum == 50:
            return "Admin"
        else:
            return "User"
        self.lfh.CloseDatabase()
        # This function generates 10 random numbers 
        # If userType is admin, the sum of the 10 random numbers is 50
        # If userType is user, the sum of the 10 random numbers is 51
    def GenerateID(self, userType):
            #Identify if userType is admin or user
            if userType == "Admin":
                _sum = 50
            else:
                _sum = 51
            #Generates 10 random numbers
            n = 10
            rnd_id = 0
            while len(str(rnd_id)) != 10:
                rnd_array = np.random.multinomial(_sum, np.ones(n)/n, size = 1)[0]
                rnd_id = ''.join(str(x) for x in rnd_array)
            return rnd_id
            
    def getEmailByUserName(self, userName):
        self.lfh.LoadDatabase()
        email = self.lfh.getEmailByUserID(self.lfh.getUserId(userName))  
        self.lfh.CloseDatabase()
        return email
    


