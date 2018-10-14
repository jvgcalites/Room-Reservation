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
        with self.conn: #if there is a connection to the database
            self.c.execute("SELECT * FROM Login WHERE UserName=:UserName",{'UserName':userName})
            if not self.c.fetchall(): #if no value is returned
                return ''
            else:
                self.c.execute("SELECT * FROM Login WHERE UserName=:UserName",{'UserName':userName})
                return self.c.fetchone()[1]
    #Returns a value if the user is an Admin or a User
    def getUserId(self, userName):
        with self.conn:
            self.c.execute("SELECT * FROM Login WHERE UserName=:UserName",
                           {'UserName':userName})
            userID = self.c.fetchone()[2]
        return userID

    def getEmailByUserID(self, userID):
        with self.conn:
            self.c.execute("SELECT * FROM User WHERE UserID=:UserID",
                          {'UserID':userID})
        return self.c.fetchone()[3]
            
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
             if not self.c.fetchall():
                 return ''
             else: 
                self.c.execute("SELECT * FROM User WHERE EmailAddress=:EmailAddress",{'EmailAddress':email})            
                return self.c.fetchall()

    def checkGivenNameExists(self, givenName):
        with self.conn:
            self.c.execute("SELECT * FROM User WHERE GivenName=:GivenName",{'GivenName':givenName})
            if not self.c.fetchall():
                return ''
            else:
                self.c.execute("SELECT * FROM User WHERE GivenName=:GivenName",{'GivenName':givenName})
                return self.c.fetchone()[1]
             
        return self.c.fetchall()    
    def UpdateDatabaseExists(self, lastName,givenName,middleName,emailAddress,password,
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
            self.c.execute("DELETE from User WHERE UserID =: UserID",{'UserID':userID})
            #Remove from Login table
            self.c.execute("DELETE from Login WHERE USerID =: UserID",{'UserID':userID})
###############################################################################
    
##############################For Users#####################################
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
    
    #Returns a string if the writing of file is successfull or not
    def AddReservation(self,natureOfActivity, org, room, month, day, year, timeIn, timeOut):
        with self.conn:
            ##############################Write to Reservation Table##########################################
            self.c.execute('INSERT INTO Reservation VALUES (?,?,?,?,?,?,?,?)', 
                           (natureOfActivity,  org, room, month, day, year, timeIn, timeOut))
            ###########################################################################################
        return "File Successfully Written!"
        
    #Returns the organization         
    def GetOrganizationDatabase(self, email):
        with self.conn:            
            self.c.execute("SELECT * FROM User WHERE EmailAddress=:EmailAddress",
                           {'EmailAddress':email})
            data = self.c.fetchone()[4]
            if not data:
                return ''
            else:
                return data
    def SchedAvailable(self, room, day, month, year):
        availability = True
        with self.conn:
            #Scan the table, if room, month, day and year matches, schedule is not available
            for row in self.c.execute("SELECT * FROM Reservation WHERE Room=? AND Month=? AND Day=? AND Year=?" , (room, month, day, year,)):
                availability = False
        return availability
<<<<<<< HEAD
    ###############################################################################
=======

>>>>>>> FRADEJAS
    
    ##############################For Schedule#####################################
    #Removes schedule with the same room, day, month, year, timeStart, and timeEnd from the passed parameters
    def RemoveSchedule(self, room, day, month, year, timeStart, timeEnd):
        with self.conn: #if there is a connection to the database
            self.c.execute("DELETE from Reservation WHERE Room =:Room AND Month =:Month AND Year =:Year AND Day=:Day AND TimeStart=:TimeStart AND TimeEnd=:TimeEnd ",
                           {'Room':room, 'Month':month,'Day':day,'Year':year,'TimeStart':timeStart,'TimeEnd':timeEnd})
    #Returns true if schedule is found with the same room, day, month, year, timeStart, and timeEnd, else false
    def SchedExists(self,room, day, month, year, timeStart, timeEnd):
        doesExists = False
        with self.conn:
            for row in self.c.execute("SELECT * FROM Reservation WHERE Room=? AND Month=? AND Day=? AND Year=? AND TimeStart=? AND TimeEnd=?" , (room, month, day, year, timeStart, timeEnd,)):
                 doesExists = True
        return doesExists
             
            
    
<<<<<<< HEAD
user = FileHandling()  
user.LoadDatabase()
print(user.GetOrganizationDatabase("daynefradejas@gmail.com"))  

print(user.SchedExists("AVR1", 6, "10", 2018, "7:30", "9:00"))

#print(user.getReservedTime("AVR1", 6, "10", 2018))
#print(user.getTimeStart("Gym", 25, "10", 2018))
#print(user.getTimeEnd("Gym", 25, "10", 2018))
#rint(user.getTimeEnd("Gym", 25, "10", 2018))

user.CloseDatabase()  
=======
>>>>>>> FRADEJAS
