#!/usr/bin/python3

import socket

SERVER_IP = "192.168.1.33"
SERVER_PORT = 9001

CHUNK_SIZE = 1024

if __name__ == "__main__":
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    address = (SERVER_IP, SERVER_PORT)
    sock.connect(address)
    msg_recv = sock.recv(CHUNK_SIZE)
    print(msg_recv.decode())
    sock.close()