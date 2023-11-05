import socket
from queue import Queue
import json
import copy
import time
import copy
from python.thread_module import ThreadWithReturnValue


SERVER  = {
    "PORT" : 5050,
    "IP" : '192.168.131.131'
}

FORMAT = "utf-8"

class User:
    def makeconnection():
        # Create a socket object
        client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

        # Connect to the server
        client_socket.connect((SERVER['IP'], SERVER['PORT']))

        # Define where you want to save the received file
        file_path = 'list.txt'

        # Receive the file data from the server and save it
        with open(file_path, 'wb') as file:
            while True:
                data = client_socket.recv(1024)
                if not data:
                    break
                file.write(data)

        print(f"File '{file_path}' received and saved.")

        # Close the socket
        client_socket.close()
client=User()
client.makeconnection()