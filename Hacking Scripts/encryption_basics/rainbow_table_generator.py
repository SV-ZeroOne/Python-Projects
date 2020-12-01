#!/usr/bin/env python

# hashlib is a useful library in python to deal with hashes
import hashlib, sys


md5Hash = hashlib.md5("Steve").hexdigest()
#print md5Hash

shaHash = hashlib.sha512("Steve").hexdigest()
#print shaHash


def md5(someString):
    return hashlib.md5(someString).hexdigest()


if len(sys.argv) != 2:
    print "[!] Python rainbow_table.py wordlist.txt"
    sys.exit()


filename = sys.argv[1]
f = open(filename,"r")
output = open("RainbowTable.txt","w")
file_data = f.readlines()


for line in file_data:
    hashed_word = hashlib.sha512(line.strip("\n")).hexdigest()
    data = "{0} : {1}".format(line.strip("\n"),hashed_word)
    output.write(data + "\n")


f.close()


#grep the rainbowTable.txt | grep SomeWord to get its hash