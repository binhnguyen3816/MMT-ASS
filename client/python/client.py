import socket
from queue import Queue
import json
import copy
import time
import copy
from python.thread_module import ThreadWithReturnValue


SERVER  = {
    "PORT" : 5050,
    "IP" : socket.gethostbyname(socket.gethostname())
}

FORMAT = "utf-8"

class User:
    pass