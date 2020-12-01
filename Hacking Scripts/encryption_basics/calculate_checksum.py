#!/usr/bin/env python

import hashlib, sys

if len(sys.argv) != 2:
    print "[!] python calculate_checksum.py filename"
    sys.exit()


filename = sys.argv[1]


def md5(someString):
    return hashlib.md5(someString).hexdigest()


def sha1(someString):
    return hashlib.sha1(someString).hexdigest()


fi = open(filename, "rb")
data = fi.read()
final_hash_md5 = md5(data)
final_hash_sha1 = sha1(data)


print "MD5 --> {0} : {1}".format(filename, final_hash_md5)
print "SHA1 --> {0} : {1}".format(filename, final_hash_sha1)