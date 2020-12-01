#!/usr/bin/env python

# pip install scapy-python3
import scapy.all as scapy
import optparse
# argparse is the successor to optparse


def scan(ip):
    # easy way
    # scapy.arping(ip)
    arp_request = scapy.ARP(pdst=ip)
    broadcast = scapy.Ether(dst="ff:ff:ff:ff:ff:ff")
    arp_request_broadcast = broadcast/arp_request
    # print(arp_request_broadcast.summary())
    # arp_request_broadcast.show()
    # arp_request.pdst = ip
    # print(arp_request.summary())
    # list the names of the variables that can be set for the ARP class
    # scapy.ls(scapy.ARP())
    # srp allows us to send a packet with a custom Ether part
    # normally returns 2 list by the [0] at the end says we just want 1 list
    answeredList = scapy.srp(arp_request_broadcast, timeout=1, verbose=False)[0]
    # print(answeredList.summary())
    clients_list = []
    for element in answeredList:
        client_dict = {"ip": element[1].psrc, "mac": element[1].hwsrc}
        # print(element[1].psrc + "\t\t" + element[1].hwsrc)
        clients_list.append(client_dict)
    return clients_list


def print_result(results_list):
    print("IP\t\t\tMAC Address\n-----------------------------------------")
    for client in results_list:
        print(client["ip"] + "\t\t" + client["mac"])


def get_arguments():
    parser = optparse.OptionParser()
    parser.add_option("-i", "--iprange", dest="iprange", help="The IP Range you want to scan")
    (options, arguments) = parser.parse_args()
    if not options.iprange:
        parser.error("[-] Please specify an iprange to scan, use --help for more info.")
    return options


user_input = get_arguments()
scan_result = scan(user_input.iprange)
print_result(scan_result)