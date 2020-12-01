#!/usr/bin/env python

# trap packets in queue using iptables -I FORWARD -j NFQUEUE --queue-num 0
# below two iptable rules are for local testing - use the above for real life min
# iptables -I OUTPUT -j NFQUEUE --queue-num 0
# iptables -I INPUT -j NFQUEUE --queue-num 0
# this is an underlying system setting and not python dependent, we will use python to read the Q
# ! will need this: pip install netfilterqueue
# needed to do this on Kali - apt-get install build-essential python-dev libnetfilter-queue-dev
# remember to iptables --flush when done

import netfilterqueue

def process_packet(packet):
    print(packet)
    packet.accept()
    # will cut traffic
    # packet.drop()


queue = netfilterqueue.NetfilterQueue()
queue.bind(0, process_packet)
queue.run



