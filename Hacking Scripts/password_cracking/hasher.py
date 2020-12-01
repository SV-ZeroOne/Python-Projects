#!/usr/bin/python

import hashlib

hashvalue = input("Enter a string to hash: ")

hashObj1 = hashlib.md5()
hashObj1.update(hashvalue.encode())
print("MD5: " + hashObj1.hexdigest())

hashObj2 = hashlib.sha1()
hashObj2.update(hashvalue.encode())
print("SHA1: " + hashObj2.hexdigest())

hashObj3 = hashlib.sha256()
hashObj3.update(hashvalue.encode())
print("SHA256: " + hashObj3.hexdigest())

hashObj4 = hashlib.sha512()
hashObj4.update(hashvalue.encode())
print("SHA512: " + hashObj4.hexdigest())
