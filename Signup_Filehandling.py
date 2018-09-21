#Author Dayne Fradejas
import sqlite3
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
        my_file = Path('Records.db')
        try:   #if database exists
            if not my_file.exists():
                raise ("Database does not exsist")
            else:
                 self.conn = sqlite3.connect('Records.db')
                 self.c = self.conn.cursor()
                 return True
        except Exception as inst: #throw exception
            print (inst)            
            return False
            
    def CloseDatabase(self):
        self.conn.close()
        
    #Returns a string if the writing of file is successfull or not
    def InsertAccount(self,lastName, givenName,middleName,emailAddress,password, organization,
                      studentNumber, contactNumber):
            with self.conn:
                userID = self.GenerateUserID() 
                ##############################Write to User Table##########################################
                self.c.execute('INSERT INTO User VALUES (?,?,?,?,?,?,?,?)',(lastName, givenName,middleName,
                               emailAddress, organization,userID, studentNumber, contactNumber))
                ###########################Write to Login Table############################################
                self.c.execute('INSERT INTO Login VALUES (?,?,?)',(emailAddress,password,userID))
                ###########################################################################################
                return "File Successfully Written!"
    def GenerateUserID(self):
        #Code to generate value
        return "Admin"
    
'''Sample Code
fh = Signup_fileHandling()
fh.LoadDatabase()
fh.InsertAccount("Fradejas",'Airon','Noche',"afradejas@gmail.com",'airon123','FilChi','2015100892','09994507120')
fh.CloseDatabase()
'''