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
###################For Users################################################
    #Returns List of details through student number
    def GetDetailsByStudentNumber(self, studentNumber):
         with self.conn: #if there is a connection to the database
            self.c.execute("SELECT * FROM User WHERE StudentNumber=:StudentNumber",{'StudentNumber':studentNumber})
            if not self.c.fetchall(): #if no value is returned
                return -1
            else:
                self.c = self.conn.cursor()
                self.c.execute("SELECT * FROM User WHERE StudentNumber=:StudentNumber",{'StudentNumber':studentNumber}) 
                value = self.c.fetchall()
                return value
    def getEmail(self,email):
         with self.conn:
             self.c.execute("SELECT * FROM User WHERE EmailAddress=:EmailAddress",{'EmailAddress':email})            
             return self.c.fetchall()

    def getGivenName(self, givenName):
        with self.conn:
             self.c.execute("SELECT * FROM User WHERE GivenName=:GivenName",{'GivenName':givenName})
        return self.c.fetchall()    
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
    def RemoveAccount(self, userID):
        with self.conn:
            #Remove from User table
            self.ahl.c.execute("DELETE from User WHERE UserID =: UserID",{'UserID':userID})
            #Remove from Login table
            self.ahl.c.execute("DELETE from Login WHERE USerID =: UserID",{'UserID':userID})
###############################################################################
##############################For Accounts#####################################
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
#        for x in range (len(time)):
#            timeTaken.append(time[x][7])   
#        return sorted(list(set(self.timeEnd)-set(timeTaken)))