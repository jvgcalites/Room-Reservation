#Author Dayne Fradejas
import sqlite3
import numpy as np
from pathlib import Path

class Signup_fileHandling:
    def __init__(self):
         self.conn = ''
         self.c = ''
    def GetPasswordByEmail(self, email):
        with self.conn: #if there is a connection to the database
            self.c.execute("SELECT * FROM Login WHERE UserName=:UserName",{'UserName':email})
            if not self.c.fetchall(): #if no value is returned
                return -1
            else:
                self.c.execute("SELECT * FROM Login WHERE UserName=:UserName",{'UserName':email})
                return self.c.fetchone()[1]
    #Load Database 
    def LoadDatabase(self):
        my_file = Path('../Database/Records.db')
        try:   #if database exists
            if not my_file.exists():
                raise ("Database does not exsist")
            else:
                 self.conn = sqlite3.connect('../Database/Records.db')
                 self.c = self.conn.cursor()
                 return True
        except Exception as inst: #throw exception
            print (inst)            
            return False
            
    def CloseDatabase(self):
        self.conn.close()
        
    #Returns a string if the writing of file is successfull or not
    def InsertAccount(self,lastName, givenName,middleName,emailAddress,password, organization,
                      studentNumber, contactNumber, userType):
            with self.conn:
                userID = self.GenerateID(userType) 
                ##############################Write to User Table##########################################
                self.c.execute('INSERT INTO User VALUES (?,?,?,?,?,?,?,?)',(lastName, givenName,middleName,
                               emailAddress, organization,userID, studentNumber, contactNumber))
                ###########################Write to Login Table############################################
                self.c.execute('INSERT INTO Login VALUES (?,?,?)',(emailAddress,password,userID))
                ###########################################################################################
                return "File Successfully Written!"
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

    
'''Sample Code
fh = Signup_fileHandling()
fh.LoadDatabase()
fh.InsertAccount("Fradejas",'Airon','Noche',"afradejas@gmail.com",'airon123','FilChi','2015100892','09994507120')
fh.CloseDatabase()
'''