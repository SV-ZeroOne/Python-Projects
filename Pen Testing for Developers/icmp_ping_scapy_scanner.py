import logging
logging.getLogger("scapy.runtime").setLevel(logging.ERROR)

import sys
from scapy.all import *

if len(sys.argv) !=3:
    print "usage: %s start_ip_addr end_ip_addr" % (sys.argv[0])
    sys.exit(0)

livehosts=[]
#IP address validation
ipregex = re.compile("^([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\.([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\.([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\.([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])$")

if (ipregex.match(sys.argv[1]) is None):
    print "Starting IP address is invalid"
    sys.exit(0)
if (ipregex.match(sys.argv[1]) is None):
    print "End IP address is invalid"
    sys.exit(0)

if not (iplist1[0]==iplist2[0] and iplist1[1]==iplist2[1] and iplist1[2]==iplist2[2])
    print "IP addresses are not in the same class C subnet"
    sys.exit(0)

if iplist1[3]>iplist2[3]:
    print "Starting IP address is greater than ending IP address"
    sys.exit(0)

networkaddr = iplist1[0]+"."+iplist1[1]+"."+iplist[2]+"."
start_ip_last_octet = int(iplist1[3])
end_ip_last_octet = int(iplist2[3])

if iplist1[3]<iplist2[3]:
    print "Pinging range "+networkaddr+str(start_ip_last_octet)+"- "+str(end_ip_last_octet)
else
    print "Pinging "+networkaddr+str(startiplastoctect)+"\n"


for x in range(start_ip_last_octet, end_ip_last_octet+1)
    packet=IP(dst=networkaddr+str(x))/ICMP()
    response = sr1(packet,timeout=2,verbose=0)
    if not (response is None):
        if response[ICMP].type==0:
            livehosts.append(networkaddr+str(x))


print "Scan complete!\n"
if len(livehosts)>0:
    print "Hosts found:\n"
    for host in livehosts:
        print host+"\n"
else:
    print "No live hosts found\n"