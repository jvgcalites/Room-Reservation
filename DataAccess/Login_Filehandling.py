
#Author Dayne Fradejas
import sqlite3
from pathlib import Path

class Login_fileHandling:
    def __init__(self):
         self.conn = ''
         self.c = ''
         
    def getPasswordByUserName(self, userName):
        self.LoadDatabase()
        with self.conn: #if there is a connection to the database
            self.c.execute("SELECT * FROM Login WHERE UserName=:UserName",{'UserName':userName})
            if not self.c.fetchall(): #if no value is returned
                return ''
            else:
                self.c.execute("SELECT * FROM Login WHERE UserName=:UserName",{'UserName':userName})
                return self.c.fetchone()[1]
        self.CloseDatabase()
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
    def getUserId(self, userName):
        self.LoadDatabase()
        with self.conn:
            self.c.execute("SELECT * FROM Login WHERE UserName=:UserName",
                           {'UserName':userName})
            userID = self.c.fetchone()[2]
        return userID
        self.CloseDatabase()
    
    def CloseDatabase(self):
        self.conn.close()
        
"""
fhl = Login_fileHandling()
fhl.LoadDatabase()
print(fhl.AccountType('vsfabesamis@mymail.mapua.edu.ph'))
fhl.CloseDatabase()
"""