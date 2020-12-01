#!/usr/bin/python3

# Script to change our Mac Address on Kali
# ifconfig eth0 down
# ifconfig eth0 hw ether 00:11:22:33:44:55
# ifconfig eth0 up
# have to run it as sudo

from mac_changer import Mac_Changer

if __name__ == "__main__":
    mc = Mac_Changer()
    mac = mc.get_MAC("eth0")
    print(mac)

    current_mac = mc.change_MAC("eth0", "00:11:22:33:44:55")
    print(current_mac)