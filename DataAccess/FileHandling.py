import sqlite3
from pathlib import Path

class FileHandling:
    
    def __init__(self):
         self.conn = ''
         self.c = ''
###############################################################################
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
    def CloseDatabase(self):
        self.conn.close()
##############################################################################
###############For Login######################################################        
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
    #Returns a value if the user is an Admin or a User
    def getUserId(self, userName):
        self.LoadDatabase()
        with self.conn:
            self.c.execute("SELECT * FROM Login WHERE UserName=:UserName",
                           {'UserName':userName})
            userID = self.c.fetchone()[2]
        return userID
        self.CloseDatabase()
    
###############################################################################
###############For Signup###################################################### 
    def InsertAccount(self,lastName, givenName,middleName,username,emailAddress,password, organization,
                          studentNumber, contactNumber, userType):
                with self.conn:
                    userID = self.GenerateID(userType) 
                    ##############################Write to User Table##########################################
                    self.c.execute('INSERT INTO User VALUES (?,?,?,?,?,?,?,?)',(lastName, givenName,middleName,
                                   emailAddress, organization,userID, studentNumber, contactNumber))
                    ###########################Write to Login Table############################################
                    self.c.execute('INSERT INTO Login VALUES (?,?,?)',(username,password,userID))
                    ###########################################################################################
                    return "File Successfully Written!"
###############################################################################
###################For Accounts################################################
    #Returns List of details through student number
    def GetDetailsByStudentNumber(self, studentNumber):
         with self.conn: #if there is a connection to the database
            self.c.execute("SELECT * FROM User WHERE StudentNumber=:StudentNumber",{'StudentNumber':studentNumber})
            return self.c.fetchall()
    def checkEmailExists(self,email):
         with self.conn:
             self.c.execute("SELECT * FROM User WHERE EmailAddress=:EmailAddress",{'EmailAddress':email})            
             data = self.c.fetchall()
             if not data:
                 return ''
             else:                  
                 return data

    def checkGivenNameExists(self, givenName):
        with self.conn:
            self.c.execute("SELECT * FROM User WHERE GivenName=:GivenName",{'GivenName':givenName})
            if not self.c.fetchall():
                return ''
            else:
                return 'value'             
        return self.c.fetchall()  
    def getUserIDByStudentNumber(self, studentNumber):
        with self.conn:
            self.c.execute("SELECT * FROM User WHERE StudentNumber=:StudentNumber",{'StudentNumber':studentNumber})
            data = self.c.fetchall()
            if not data:
                return ''
            else:
                return data[0][5]
    def getPasswordByUserID(self, userID):
        with self.conn:
            self.c.execute("SELECT * FROM Login WHERE UserID=:UserID",{'UserID':userID})
            data = self.c.fetchall()
            if not data:
                return ''
            else:
                return data[0][1]
    def UpdateDatabase(self, lastName,givenName,middleName,emailAddress,password,
                       organization,studentNumber,contactNumber,userID):
        with self.conn:
            self.c.execute('''UPDATE User SET 
                           LastName=:LastName,
                           GivenName=:GivenName,
                           MiddleName=:MiddleName,
                           EmailAddress=:EmailAddress, 
                           Organization=:Organization,
                           ContactNumber=:ContactNumber 
                           WHERE StudentNumber=:StudentNumber''',
                           {'LastName':lastName,
                            'GivenName':givenName, 
                            'MiddleName':middleName,
                            'EmailAddress':emailAddress,
                            'Organization':organization, 
                            'ContactNumber':contactNumber,
                            'StudentNumber':studentNumber})
    
            self.c.execute('''UPDATE Login SET
                           Password=:Password, UserName=:UserName
                           WHERE UserID=:UserID''',{
                           'Password':password,'UserName':emailAddress,'UserID':userID})
    
    def getEmailAddressByStudentNumber(self, studentNumber):
        with self.conn:
            self.c.execute("SELECT * FROM User WHERE StudentNumber = :StudentNumber",
                           {'StudentNumber':studentNumber})
            data = self.c.fetchall()           
            if not data:
                return ''
            else:
                return data[0][3]
            return 'value'
        
    def checkLastNameExists(self, lastName):
        with self.conn:
            self.c.execute("SELECT * FROM User WHERE LastName = :LastName",
                               {'LastName':lastName})
            if not self.c.fetchall():
                return ''
            else:
                return 'value'
            
    def RemoveAccount(self, userID):
        with self.conn:
            #Remove from User table
            self.c.execute("DELETE FROM User WHERE UserID = :UserID",{'UserID':userID})
            #Remove from Login table
            self.c.execute("DELETE FROM Login WHERE USerID = :UserID",{'UserID':userID})
            self.conn.commit()
###############################################################################    
#################################For Users#####################################
    def checkyEmailExists(self, email):
        with self.conn:
             self.c.execute("SELECT * FROM User WHERE EmailAddress=:EmailAddress",{'EmailAddress':email})        
        if not self.c.fetchall():
            return ''
        else:
            return 'Ok'

    def checkNameExists(self, lastName,givenName):
            with self.conn:
                 self.c.execute('''SELECT * FROM User WHERE GivenName=:GivenName
                                AND LastName =:LastName''',{'GivenName':givenName , 'LastName':lastName})        
            if not self.c.fetchall():
                return ''
            else:
                return 'something'        
    def getReservedTime(self, room, day, month, year):
        with self.conn: #if there is a connection to the database
            self.c.execute("SELECT * FROM Reservation WHERE Room = :Room AND Month = :Month AND Year =:Year AND Day= :Day ",
                           {'Room':room, 'Month':month,'Day':day,'Year':year})
            return  self.c.fetchall()           
        
    def getTimeStart(self, room, day, month, year):
        self.c.execute("SELECT * FROM Reservation WHERE Room = :Room AND Month = :Month AND Year =:Year AND Day= :Day ",
                           {'Room':room, 'Month':month,'Day':day,'Year':year})
        return self.c.fetchall()

        
    def getTimeEnd(self, room, day, month, year):
#        timeTaken = []
        self.c.execute("SELECT * FROM Reservation WHERE Room = :Room AND Month = :Month AND Year =:Year AND Day= :Day ",
                           {'Room':room, 'Month':month,'Day':day,'Year':year})
        return self.c.fetchall()
