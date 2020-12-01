#sniffing tool
import socket

#create an INET, raw packet

soc = socket.socket(socket.AF_INET, socket.SOCK_RAW, socket.IPPROTO_TCP)

# recieve a packet
while True:
    print(soc.recvfrom(65565))