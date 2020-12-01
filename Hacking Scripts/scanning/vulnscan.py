#!/usr/bin/python
# code from https://www.udemy.com/course/ethical-hacking-python/learn/lecture/14295120#overview
# this code uses a file which contains vulnurable banners and then checks if any of the targets have these banner by doing a port scan

import socket
import os
import sys


def returnBanner(ip,port):
    try: 
	    socket.setdefaulttimeout(2)
        s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        s.connect((ip,port))
        banner = s.recv(1024)
        return banner
    except:
	#print "[-] Could not retrieve banner for port: " + str(port)
        return


def checkVulns(banner, filename):
    f = open(filename, "r")
    for line in f.readlines():
        if line.strip("\n") in banner:
            print '[+] Server has vulnurable app: ' + banner.strip("\n")


def main():
    if len(sys.argv) == 2:
        filename = sys.argv[1]
        if not os.path.isfile(filename):
            print "[-] File does not exist!"
            exit(0)
        if not os.access(filename, os.R_OK):
            print '[-] Access Denied'
            exit(0)
    else:
        print '[-] Usage: ' + str(sys.argv[0]) + " <vuln filename>"
        exit(0)

    portlist = [21,22,25,80,110,443,445,8080,3306]
    # scan multiple targets in IP range below
    for x in range(10,20)
        ip = "10.0.2." + srt(x)
        for port in portlist:
            banner = returnBanner(ip, port)
            if banner:
                print '[+] ' + ip "/" str(port) + " : " + banner
                checkVulns(banner, filename)


main()