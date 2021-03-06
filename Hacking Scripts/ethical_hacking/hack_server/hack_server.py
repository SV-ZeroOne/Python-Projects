#!/usr/bin/python3

import socket


SERVER_IP = "192.168.1.33"
SERVER_PORT = 9001

if __name__ == "__main__":

    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    address = (SERVER_IP, SERVER_PORT)
    sock.bind(address)
    sock.listen(1)
    print("[+] Waiting for incoming connections: ", SERVER_PORT)
    client_sock, client_add = sock.accept()
    print("[+] Connection established from: ", client_add)
    msg = "This is the server speaking"
    client_sock.send(msg.encode())
    client_sock.close()
    sock.close()