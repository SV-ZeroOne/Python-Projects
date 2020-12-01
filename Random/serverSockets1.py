import socket
#create a socket object
s = socket.socket()
print('Socket successfully created.')

#reserve a port number on the host machine
port = 12345

#bind to the port
s.bind(('',port))
print('Socket binded to %s' %(port))

#put the socket into listening mode
s.listen(4)
print('Socket is now listening')

#a forever loop until exit or an error occurs
# establish a connection with client
while True:
    c, addr = s.accept()
    print('Got connect from', addr)