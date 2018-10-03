
#Author Dayne Fradejas
import sqlite3
from pathlib import Path

class Login_fileHandling:
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
    #Returns a value if the user is an Admin or a User
    def AccountType(self, email):
        with self.conn:
            self.c.execute("SELECT * FROM User WHERE EmailAddress=:EmailAddress",
                           {'EmailAddress':email})
            userID = self.c.fetchone()[5]
        #adds the string of numbers from userID
        _sum = sum(map(int,userID))
        if _sum == 50:
            return "Admin"
        else:
            return "User"
            
    def CloseDatabase(self):
        self.conn.close()
        
