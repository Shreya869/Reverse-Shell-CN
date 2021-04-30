#Step 1: Creating a socket

#importing libraries
import socket 
import sys

#Create a socket (Connect two computers)

def create_socket():
  try:
    
      global host
      global port
      global s
      host = " "
      port = 9999
      s = socket.socket()
      
   except socket.error as msg:
       print("Socket creation error: " + str(msg))
