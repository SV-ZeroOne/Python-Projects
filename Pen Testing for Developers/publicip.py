#!/usr/bin/env python
'''
Author: Christopher Duffy
Date: February 2015
Name: publicip.py
Purpose: To grab your current public IP address

https://raw.githubusercontent.com/funkandwagnalls/pythonpentest/master/publicip.py
'''

import urllib2

def get_public_ip(request_target):
    grabber = urllib2.build_opener()
    grabber.addheaders = [('User-agent','Mozilla/5.0')]
    try:
        public_ip_address = grabber.open(target_url).read()
    except urllib2.HTTPError, error:
        print("There was an error trying to get your Public IP: %s") % (error)
    except urllib2.URLError, error:
        print("There was an error trying to get your Public IP: %s") % (error)
    return public_ip_address

public_ip = "None"
target_url = "http://ip.42.pl/raw"
public_ip = get_public_ip(target_url)

if not "None" in public_ip:
    print("Your Public IP address is: %s") % (str(public_ip))
else:
    print("Your Public IP address was not found")