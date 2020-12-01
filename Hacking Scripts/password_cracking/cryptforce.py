#!/usr/bin/python
#python 3

import crypt
from termcolor import colored


def crackPass(cryptWord):
    salt = cryptWord[0:2]
    dictionary = open("dictionary.txt",'r')
    for word in dictionary.readlines():
        word = word.strip('\n')
        cryptPass = crypt.crypt(word,salt)
        if cryptWord == cryptPass:
            print(colored('[+] Found Password: ' + word),'red')
            return True


def main():
    passFile = open('pass.txt', 'r')
    for line in passFile.readlines():
        if ":" in line:
            user = line.split(":")[0]
            cryptWord = line.split(":")[1]
            #print cryptWord
            print(colored("[+] Cracking Password for: " + user),'green')
            crackPass(cryptWord):


main()