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
    pass