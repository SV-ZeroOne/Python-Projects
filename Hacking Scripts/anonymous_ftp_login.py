#!/usr/bin/python
# some servers allow for anonymous login

import ftplib


def anonLogin(hostname):
    try:
        ftp = ftplib.FTP(hostname)
        ftp.login('anonymous', 'anonymous')
        print "[+] " + hostname + " FTP Anonymous login succeded"
    except Exception, e:
        print "[-] " + hostname + " FTP Anonymous login failed"


host = raw_input("Enter the host IP address: ")
anonLogin(host)