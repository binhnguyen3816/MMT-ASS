import socket
# import pandas as pd
import json
import copy
from thread_module import *
from dbms import dbms

FORMAT = "utf-8"

print('server host', socket.gethostbyname(socket.gethostname()))

SERVER  = {
    "PORT" : 5050,
    "IP" : socket.gethostbyname(socket.gethostname())
}

class Server:
    def __init__(self):
        self.server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.server.bind((SERVER["IP"], SERVER["PORT"]))
        self.server.listen(20)
        self.online = {}
        # self.sender_mutex = Lock()
    def show(self):
        dbms.show()
    def discover(self, hostname):
        dbms.peek(hostname)
    
server=Server()