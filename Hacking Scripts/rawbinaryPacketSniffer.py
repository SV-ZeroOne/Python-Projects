import socket
#not working for some reason

#create raw packet object (sniffer)
sniffer = socket(socket.AF_INET, socket.SOCK_RAW, socket.IPPROTO_ICMP, 1)

#bind it to a host
sniffer.bind(('0.0.0.0', 0)) 

#make sure that IP header is included also
sniffer.setsockopt(socket.IPPROTO_IP, socket.IP_HDRINCL,1)

print('sniffer is listening for incoming connections')
#get a single packet
print(sniffer.recvfrom(65535))
