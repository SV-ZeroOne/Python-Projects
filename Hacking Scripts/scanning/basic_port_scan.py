#!/usr/bin/python3
#use python 3

import socket
from termcolor import colored

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
socket.setdefaulttimeout(1)

host = input("[*] Enter the host IP to scan: ")
#port = int(input("[*] Enter the port to scan: "))

def portScanner(port):
    if sock.connect_ex((host,port)):
        print(colored("Port %d is closed" % (port), 'red'))
    else:
        print(colored("Port %d is open" % (port), 'green'))


for port in range(1, 65535):
    portScanner(port)