#connect to google and ping them
import socket
import sys

try:
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    print('Socket successfully created')
except socket.error as err:
    print('Socket creation failed with an error %s' %(err))

#default port for the socket
port = 80

try:
    host_ip = socket.gethostbyname('www.google.com')
except socket.gaierror:
    print('there was an error resolving the host')
    sys.exit()

#conneting to the server
s.connect((host_ip, port))
print('the socket has successfully connected to google \ on ip address == %s'%(host_ip))