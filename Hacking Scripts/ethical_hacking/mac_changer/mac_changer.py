#!/usr/bin/python3

# Script to change our Mac Address on Kali
# ifconfig eth0 down
# ifconfig eth0 hw ether 00:11:22:33:44:55
# ifconfig eth0 up
# have to run it as sudo

import subprocess
import re

class Mac_Changer:
    def __init__(self):
        self.MAC = ""

    def get_MAC(self, iface):
        output = subprocess.run(["ifconfig", iface], shell=False, capture_output=True)
        cmd_result = output.stdout.decode('utf-8')
        print(cmd_result)
        # Regex pattern to grab the MAC address from the ifconfig output
        pattern = r'ether\s[\da-z]{2}:[\da-z]{2}:[\da-z]{2}:[\da-z]{2}:[\da-z]{2}:[\da-z]{2}'
        regex_string = re.compile(pattern)
        result = regex_string.search(cmd_result)
        # print(result)
        # Split off the MAC from the ether word
        current_mac = result.group().split(" ")[1]
        self.MAC = current_mac
        return current_mac

    def change_MAC(self, iface, new_mac):
        print("[+] Current MAC: ", self.get_MAC(iface))
        output = subprocess.run(["ifconfig", iface, "down"], shell=False, capture_output=True)
        # If there is no output then everything is fine otherwise print out the error
        print(output.stderr.decode('utf-8'))
        output = subprocess.run(["ifconfig", iface, "hw", "ether", new_mac], shell=False, capture_output=True)
        print(output.stderr.decode('utf-8'))
        output = subprocess.run(["ifconfig", iface, "up"], shell=False, capture_output=True)
        print(output.stderr.decode('utf-8'))
        print("[+] New MAC: ", self.get_MAC(iface))
        return self.get_MAC(iface)