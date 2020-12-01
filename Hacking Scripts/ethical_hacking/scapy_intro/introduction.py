#!/usr/bin/python3
# Scapy is a python library that allows us to design, manipulate, intercept and process packets
# Scapy sets header fields by default.
# Have to be root to run this.

from scapy.all import IP, ICMP, sr1, ls

ip_layer = IP(src="192.168.0.1", dst="www.google.com")

#print(ip_layer.show())

icmp_req = ICMP()

# Help to list (ls) details about the layer.
print(ls(ip_layer))
print(ip_layer.show())
print(ip_layer.summary())

print(icmp_req.show())
# Add the layers together with /
packet = ip_layer / icmp_req
#print(packet.show())
received_packet = sr1(packet)

if received_packet:
    print(received_packet.show())