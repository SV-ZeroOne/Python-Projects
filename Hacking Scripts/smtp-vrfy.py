#!/usr/bin/python
import socket
import sys

if len(sys.argv) != 2:
    print "Usage: vrfy.py <username-list.txt>"
    sys.exit(0)


# Create a Socket
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# Connect to the Server
connect = s.connect(('10.11.1.217',25))
# Receive the banner
banner = s.recv(1024)
print banner
usernames = open(sys.argv[1], 'r')
for username in usernames:
    # VRFY a user
    user = username.strip('\r').strip('\n')
    s.send('VRFY ' + user + '\r\n')
    result = s.recv(1024)
    print result


# Close the socket
s.close()
