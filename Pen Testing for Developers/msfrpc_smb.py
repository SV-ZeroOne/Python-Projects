#!/usr/bin/env python
'''
Author: Christopher Duffy
Date: March 2015
Name: msfrpc_smb.py
Purpose: To scan a network for a smb ports and validate if credentials work on the target host

Copyright (c) 2015, Christopher Duffy All rights reserved.

Redistribution and use in source and binary forms, with or without modification, 
are permitted provided that the following conditions are met: * Redistributions 
of source code must retain the above copyright notice, this list of conditions and 
the following disclaimer. * Redistributions in binary form must reproduce the above 
copyright notice, this list of conditions and the following disclaimer in the 
documentation and/or other materials provided with the distribution. * Neither the 
name of the nor the names of its contributors may be used to endorse or promote 
products derived from this software without specific prior written permission.

THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS 
"AS IS" AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, 
THE IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE ARE 
DISCLAIMED. IN NO EVENT SHALL CHRISTOPHER DUFFY BE LIABLE FOR ANY DIRECT, INDIRECT, 
INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT LIMITED TO, 
PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES; LOSS OF USE, DATA, OR PROFITS; OR BUSINESS 
INTERRUPTION) HOWEVER CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT 
LIABILITY, OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE 
OF THIS SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.
'''

import os, argparse, sys, time
try:
    import msfrpc
except:
    sys.exit("[!] Install the msfrpc library that can be found here: https://github.com/SpiderLabs/msfrpc.git")
try:
    import nmap
except:
    sys.exit("[!] Install the nmap library: pip install python-nmap")
try:
    import netifaces
except:
    sys.exit("[!] Install the netifaces library: pip install netifaces")

def get_interfaces():
    interfaces = netifaces.interfaces()
    return interfaces

def get_gateways():
    gateway_dict = {}
    gws = netifaces.gateways()
    for gw in gws:
        try:
            gateway_iface = gws[gw][netifaces.AF_INET]
            gateway_ip, iface = gateway_iface[0], gateway_iface[1]
            gw_list =[gateway_ip, iface]
            gateway_dict[gw]=gw_list
        except:
            pass
    return gateway_dict

def get_addresses(interface):
    addrs = netifaces.ifaddresses(interface)
    link_addr = addrs[netifaces.AF_LINK]
    iface_addrs = addrs[netifaces.AF_INET]
    iface_dict = iface_addrs[0]
    link_dict = link_addr[0]
    hwaddr = link_dict.get('addr')
    iface_addr = iface_dict.get('addr')
    iface_broadcast = iface_dict.get('broadcast')
    iface_netmask = iface_dict.get('netmask')
    return hwaddr, iface_addr, iface_broadcast, iface_netmask

def get_networks(gateways_dict):
    networks_dict = {}
    for key, value in gateways_dict.iteritems():
        gateway_ip, iface = value[0], value[1]
        hwaddress, addr, broadcast, netmask = get_addresses(iface)
        network = {'gateway': gateway_ip, 'hwaddr' : hwaddress, 'addr' : addr, 'broadcast' : broadcast, 'netmask' : netmask}
        networks_dict[iface] = network
    return networks_dict

def target_identifier(verbose, dir, user, passwd, ips, port_num, ifaces, ipfile):
    hostlist = []
    pre_pend = "smb"
    service_name = "microsoft-ds"
	service_name2 = "netbios-ssn"
    protocol = "tcp"
    port_state = "open"
    bufsize = 0
    hosts_output = "%s/%s_hosts" % (dir, pre_pend)
    scanner = nmap.PortScanner()
    if ipfile != None:
	    if verbose > 0:
		    print("[*] Scanning for hosts from file %s") % (ipfile)
        with open(ipfile) as f:
            hostlist = f.read().replace('\n',' ')
        scanner.scan(hosts=hostlist, ports=port_num)
    else:
	    if verbose > 0:
		    print("[*] Scanning for host\(s\) %s") % (ips)
        scanner.scan(ips, port_num)
    open(hosts_output, 'w').close()
    hostlist=[]
    if scanner.all_hosts():
        e = open(hosts_output, 'a', bufsize)
    else:
        sys.exit("[!] No viable targets were found!")
    for host in scanner.all_hosts():
        for k,v in ifaces.iteritems():
            if v['addr'] == host:
                print("[-] Removing %s from target list since it belongs to your interface!") % (host)
                host = None
        if host != None:
            e = open(hosts_output, 'a', bufsize)
            if service_name or service_name2 in scanner[host][protocol][int(port_num)]['name']:
                if port_state in scanner[host][protocol][int(port_num)]['state']:
                    if verbose > 0:
                        print("[+] Adding host %s to %s since the service is active on %s") % (host, hosts_output, port_num)
                    hostdata=host + "\n"
                    e.write(hostdata)
                    hostlist.append(host)
		else:
		    if verbose > 0:
			    print(print("[-] Host %s is not being added to %s since the service is not active on %s") % (host, hosts_output, port_num))
    if not scanner.all_hosts():
        e.closed
    if hosts_output:
        return hosts_output, hostlist

def build_command(verbose, user, passwd, dom, port, ip):
    module = "auxiliary/scanner/smb/smb_enumusers_domain"
    command = '''use ''' + module + '''
set RHOSTS ''' + ip + '''
set SMBUser ''' + user + '''
set SMBPass ''' + passwd + '''
set SMBDomain ''' + dom +'''
run
'''
    return command, module

def run_commands(verbose, iplist, user, passwd, dom, port, file):
    bufsize = 0
    e = open(file, 'a', bufsize)
    done = False
    client = msfrpc.Msfrpc({})
    client.login('msf','msfrpcpassword')
    try:
        result = client.call('console.create')
    except:
        sys.exit("[!] Creation of console failed!")
    console_id = result['id']
    console_id_int = int(console_id)
    for ip in iplist:
        if verbose > 0:
            print("[*] Building custom command for: %s") % (str(ip))
        command, module = build_command(verbose, user, passwd, dom, port, ip)
        if verbose > 0:
            print("[*] Executing Metasploit module %s on host: %s") % (module, str(ip))
        client.call('console.write',[console_id, command])
        time.sleep(1)
        while done != True:
            result = client.call('console.read',[console_id_int])
            if len(result['data']) > 1:
                if result['busy'] == True:
                    time.sleep(1)
                    continue
                else:
                    console_output = result['data']
                    e.write(console_output)
                    if verbose > 0:
                        print(console_output)
                    done = True
    e.closed
    client.call('console.destroy',[console_id])

def main():
    # If script is executed at the CLI
    usage = '''usage: %(prog)s [-u username] [-p password] [-d domain] [-t IP] [-l IP_file] [-r ports] [-o output_dir] [-f filename] -q -v -vv -vvv'''
    parser = argparse.ArgumentParser(usage=usage)
    parser.add_argument("-u", action="store", dest="username", default="Administrator", help="Accepts the username to be used, defaults to 'Administrator'")
    parser.add_argument("-p", action="store", dest="password", default="admin", help="Accepts the password to be used, defalts to 'admin'")
    parser.add_argument("-d", action="store", dest="domain", default="WORKGROUP", help="Accepts the domain to be used, defalts to 'WORKGROUP'")
    parser.add_argument("-t", action="store", dest="targets", default=None, help="Accepts the IP  to be used, can provide a range, single IP or CIDR")
    parser.add_argument("-l", action="store", dest="targets_file", default=None, help="Accepts a file with IP addresses, ranges, and CIDR notations delinated by new lines")
    parser.add_argument("-r", action="store", dest="ports", default="445", help="Accepts the port to be used, defalts to '445'")
    parser.add_argument("-o", action="store", dest="home_dir", default="/root", help="Accepts the dir to store any results in, defaults to /root")
    parser.add_argument("-f", action="store", dest="filename", default="results", help="Accepts the filename to output relevant results")
    parser.add_argument("-v", action="count", dest="verbose", default=1, help="Verbosity level, defaults to one, this outputs each command and result")
    parser.add_argument("-q", action="store_const", dest="verbose", const=0, help="Sets the results to be quiet")
    parser.add_argument('--version', action='version', version='%(prog)s 0.42b')
    args = parser.parse_args()

    # Argument Validator
    if len(sys.argv)==1:
        parser.print_help()
        sys.exit(1)

    if (args.targets == None) and (args.targets_file == None):
        parser.print_help()
        sys.exit(1)

    # Set Constructors
    verbose = args.verbose             # Verbosity level
    password = args.password           # Password or hash to test against default is admin
    username = args.username           # Username to test against default is Administrator
    domain = args.domain               # Domain default is WORKGROUP
    ports = args.ports                 # Port to test against Default is 445
    targets = args.targets             # Hosts to test against
    targets_file = args.targets_file   # Hosts to test against loaded by a file
    home_dir = args.home_dir           # Location to store results
    filename = args.filename           # A file that will contain the final results
    gateways = {}
    network_ifaces={}

    if not filename:
        if os.name != "nt":
             filename = home_dir + "/msfrpc_smb_output"
        else:
             filename = home_dir + "\\msfrpc_smb_output"
    else:
        if filename:
            if "\\" or "/" in filename:
                if verbose > 1:
                    print("[*] Using filename: %s") % (filename)
        else:
            if os.name != "nt":
                filename = home_dir + "/" + filename
            else:
                filename = home_dir + "\\" + filename
                if verbose > 1:
                    print("[*] Using filename: %s") % (filename)

    gateways = get_gateways()
    network_ifaces = get_networks(gateways)
    hosts_file, hostlist = target_identifier(verbose, home_dir, username, password, targets, ports, network_ifaces, targets_file)
    run_commands(verbose, hostlist, username, password, domain, ports, filename)

if __name__ == '__main__':
    main()