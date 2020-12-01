#!/usr/bin/python
# very simple program that sniffs DNS packet and prints it out

from scapy.all import *


def findDNS(pac):
    if pac.haslayer(DNS):
        print pac[IP].src, pac[DNS].summary()


sniff(prn=findDNS)