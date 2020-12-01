#!/usr/bin/python

import socket


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


def main():
    ip = raw_input("[*] Enter Target IP: ")
    for port in range(1,10000):
        banner = returnBanner(ip,port)
        if banner:
            print "[+]" + ip + "/" + str(port) + " : " + banner.strip('\n')


main()
