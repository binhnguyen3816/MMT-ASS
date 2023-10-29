from database import fileSharingApp
import copy

class DBMS:
    def __init__(self):
        pass
    def Login(self, username, password):
        for dataTuple in fileSharingApp.client:
            if dataTuple['username'] == username and dataTuple['password'] == password:
                return True
                #UpdateHostName(IP)
        return False
        
    def Signup(self,username, password, IP):
        for dataTuple in fileSharingApp.client:
            if dataTuple['username'] == username:
                return True #username already exist
            
        fileSharingApp.client.append({'username':username, 'password':password, 'IP': IP})
        return False 
    
    
dbms = DBMS()