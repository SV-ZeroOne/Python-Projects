#!/usr/bin/python
# python 3

from urllib.request import urlopen
import hashlib
from termcolor import colored


def tryOpenFile(wordList):
    global passFile 
    try:
        passFile = open(wordList, "r")
    except:
        print("[-] No such file at that path! ")
        quit()


passHash = input("[+] Enter MD5 hash value: ")
wordList = input("[+] Enter path to the password file: ")
tryOpenFile(wordList)

for word in passFile:
    print(colored("[-] Trying: " + word.strip("\n"), 'red'))
    encodeWord = word.encode('utf-8')
    md5digest = hashlib.md5(encodeWord.strip().hexdigest())

    if md5digest == passHash:
        print(colored("[+] Password found: " + word),'green')
        exit(0)

print("[!] Password not in list!")
