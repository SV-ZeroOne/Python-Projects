#!/usr/bin/env python

import subprocess
import optparse
import re


def get_arguments():
    # https://docs.python.org/2/library/optparse.html
    parser = optparse.OptionParser()
    parser.add_option("-i", "--interface", dest="interface", help="Interface name to change its MAC address")
    parser.add_option("-m", "--mac", dest="new_mac", help="New MAC address to change to")
    (options, arguments) = parser.parse_args()
    # check if options.interface does not contain a value
    if not options.interface:
        parser.error("[-] Please specify an interface, use --help for more info.")
    elif not options.new_mac:
        parser.error("[-] Please specify an new mac address, use --help for more info.")
    return options


def change_mac(interface, new_mac):
    print("Changing MAC address for: " + interface + " to " + new_mac)
    # this is a match better way to do it as it will prevent user input error and prevent hijack of the flow
    subprocess.call(["ifconfig", interface, "down"])
    subprocess.call(["ifconfig", interface, "hw", "ether", new_mac])
    subprocess.call(["ifconfig", interface, "up"])


def get_current_mac(interface):
    ifconfig_result = subprocess.check_output(["ifconfig", interface])
    # print(ifconfig_result)
    # Generated the below regex rule with https://pythex.org/ to find mac address in ifconfig output
    mac_address_search_result = re.search(r"\w\w:\w\w:\w\w:\w\w:\w\w:\w\w", ifconfig_result)
    # first group/result
    if mac_address_search_result:
        return mac_address_search_result.group(0)
    else:
        print("[-] Could not read mac address.")


options = get_arguments()
current_mac = get_current_mac(options.interface)
print("Current MAC: " + str(current_mac))

change_mac(options.interface, options.new_mac)
# variable gets overwritten here wil the new mac address
current_mac = get_current_mac(options.interface)
if current_mac == options.new_mac:
    print("[+] MAC Address was changed to : " + current_mac)
else:
    print("[-] MAC Address did not get changed.")


# this input method is python3 dependant - input("interface > ")
# python 2 we can use raw_input - https://docs.python.org/2/library/functions.html#raw_input
# interface = raw_input("interface > ")
# new_mac = raw_input("new MAC > ")
# interface = options.interface,
# new_mac = options.new_mac

# subprocess.call("ifconfig", shell=True)
# subprocess.call("ifconfig " + interface + " down", shell=True)
# subprocess.call("ifconfig " + interface + " hw ether " + new_mac, shell=True)
# subprocess.call("ifconfig " + interface + " up", shell=True)
# subprocess.call("ifconfig", shell=True)

