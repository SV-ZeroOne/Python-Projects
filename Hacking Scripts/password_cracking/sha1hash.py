#!/usr/bin/python
# python 3
# password lists https://github.com/danielmiessler/SecLists/tree/master/Passwords/Common-Credentials

from urllib.request import urlopen
import hashlib
from termcolor import colored


sha1hash = input("[*] Enter SHA1 Hash value: ")

# get the raw git download links to use for a password list
passlist = str(urlopen('https://raw.githubusercontent.com/danielmiessler/SecLists/master/Passwords/Common-Credentials/10-million-password-list-top-10000.txt').read(), 'utf-8')

for word in passlist.split('\n'):
    hashguess = hashlib.sha1(bytes(word, 'utf-8')).hexdigest()
    if hashguess == sha1hash:
        print(colored('[+] The Password is: ' + str(word), 'green'))
        quit()
    else:
        print(colored("[-] Password guess: " + str(word) + " does not match, trying next...",'red'))

print("Password no in passwordlist")
