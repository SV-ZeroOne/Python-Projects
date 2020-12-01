import socket, sys

host = sys.argv[1]
port = int(sys.argv[2])
#socket.AF_INET = ipv4 and socket.SOCK_STREAM = TCP connection
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
try:
    sock.connect((host,port))
    print("[+] Connection Made!")
except socket.error:
    print("[+] Error happend/")

#Send data to the host specified above.
#Only works with Python 2 and not 3 - On 3 it causes TypeError: a bytes-like object is required, not 'str'
sock.send("Hi\n")