#Creating a simple Web Server
#Only seems to work with Python 3 interpreter
import socket

HOST, PORT = '', 8888

listen_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
listen_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
listen_socket.bind((HOST, PORT))
listen_socket.listen(1)

print('Serving HTTP on port %s ...' %PORT)

while True:
    client_connection, client_address = listen_socket.accept()
    request = client_connection.recv(1024)
    print(request.decode('utf-8'))
    
    http_response = """\
HTTP/1.1 200 OK

Hello World - This is my simple python server.
"""
    client_connection.sendall(bytes(http_response, 'utf-8'))
    client_connection.close()