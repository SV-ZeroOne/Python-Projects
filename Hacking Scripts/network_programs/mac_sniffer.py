#!/usr/bin/python

import socket
from struct import *
# https://docs.python.org/2/library/struct.html


def eth_addr(packet):
    b = "%.2x:%.2x:%.2x:%.2x:%.2x:%.2x" % (ord(packet[0]), ord(packet[1]), ord(packet[2]), ord(packet[3]), ord(packet[4]), ord(packet[5]))
    return b


try:
    # AF_PACKET allows us to maniuplate the packet at packet level
    s = socket.socket(socket.AF_PACKET, socket.SOCK_RAW, socket.ntohs(0x0003))
except:
    print("[!] Error on creating socket object")
    exit(0)


while True:
    packet = s.recvfrom(65535)
    packet = packet[0]

    eth_length = 14
    eth_header = packet[:eth_length]

    eth = unpack('!6s6sH',eth_header)
    eth_protocol = socket.ntohs(eth[2])
    print('[+] Destination MAC: ' + eth_addr(packet[0:6]) + ' [+] Source MAC: ' + eth_addr(packet[6:12]) + ' [+] Protocol: ' + str(eth_protocol))