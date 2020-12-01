#!/usr/bin/python
# python 3
# this program uses the default linux command line arguments to change the MAC address

import subprocess


def changeMacAddress(interface, address):
    subprocess.call(["ifconfig " + interface + " down"])
    subprocess.call(["ifconfig " + interface + " hw ether " + address])
    subprocess.call(["ifconfig " + interface + " up"])


def main():
    interface = input("[*] Enter the interface to change the MAC address on: ")
    new_mac_address = input("[+] Enter the new MAC address to change to: ")
    before_change = subprocess.check_output(["ifconfig " + interface])
    changeMacAddress(interface, new_mac_address)
    after_change = subprocess.check_output(["ifconfig " + interface])

    if before_change == after_change:
        print("[!] Failed to change MAC address to: " + new_mac_address)
    else:
        print("[*] MAC address changed to: " + new_mac_address + " on interface " + interface)


main()