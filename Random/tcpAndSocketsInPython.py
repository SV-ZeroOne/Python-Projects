#TCP Clients in python
#Creation of sockets
import socket

#Create socket object
s = socket.socket()
print("Socket successfully created")
#reserve a port
port = 1989
#bind to port
s.bind(('',port))
print('Socket binded to port: %s'%(port))
#put the soccket into listening mode
s.listen(5)
print("Socket is now listening")
#a forever loop until we exit
while True:
    #establish connection with client
    c, addr = s.accept()
    print ('Got connection from', addr)