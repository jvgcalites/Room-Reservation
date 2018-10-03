# -*- coding: utf-8 -*-
"""
Created on Sun Sep 23 12:36:06 2018

@author: jvgca
"""

class UserInfo:
    
    def __init__ (self, lname, gname, mname, email, pw, org, studNum, contactNum, userType ):
        self.lastName = lname
        self.givenName = gname
        self.middleName = mname
        self.emailAddress = email
        self.password = pw
        self.organization = org
        self.studentNumber =studNum
        self.contactNumber = contactNum
        self.userType = userType
