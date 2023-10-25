from database import chatapp
import copy

class DBMS:
    def __init__(self):
        pass
    def checkLogin(self, username, password):
        for d in chatapp.authentication:
            if d['username'] == username and d['password'] == password:
                return True
        return False
        
    def checkSignup(self,username, pw):
        for d in chatapp.authentication:
            if d['username']==username:
                return True #already exist
            
        chatapp.authentication.append({'username':username, 'password':pw})
        return False 
    
    
dbms = DBMS()