#!/usr/bin/env python
'''
Author: Christopher Duffy
Date: April 2015
Name: headrequest.py
Purpose: To identify live web applications out extensive IP ranges

Copyright (c) 2015, Christopher Duffy All rights reserved.

When assessing large environments to include Content Delivery Networks (CDN),
you will find that you will be identifying hundreds of open web ports. Most of these
web ports have no active web applications deployed on those ports, so you need to
either visit each page or request the web page header. This can simply be done by
executing a HEAD request to both the http:// and https:// versions of the site. A
Python script that uses urllib2 can execute this very easily. This script simply takes
a file of the host Internet Protocol (IP) addresses, which then builds the strings that
create the relevant Uniform Resource Locator (URL). As each site is requested, if it
receives a successful request, the data is written to a file:
'''

import urllib2, argparse, sys

def host_test(filename):
    file = "headrequests.log"
    bufsize = 0
    e = open(file, 'a', bufsize)
    print("[*] Reading file %s") % (file)
    with open(filename) as f:
        hostlist = f.readlines()
    for host in hostlist:
        print("[*] Testing %s") % (str(host))
        target = "http://" + host
        target_secure = "https://" + host
        try:
            request = urllib2.Request(target)
            request.get_method = lambda : 'HEAD'
            response = urllib2.urlopen(request)
        except:
            print("[-] No web server at %s") % (str(target))
            response = None
        if response != None:
            print("[*] Response from %s") % (str(target))
            print(response.info())
            details = response.info()
            e.write(str(details))
        try:
            request_secure = urllib2.urlopen(target_secure)
            request_secure.get_method = lambda : 'HEAD'
            response_secure = urllib2.urlopen(request_secure)
        except:
            print("[-] No web server at %s") % (str(target_secure))
            response_secure = None
        if response_secure != None:
            print("[*] Response from %s") % (str(target_secure))
            print(response_secure.info())
            details = response_secure.info()
            e.write(str(details))
    e.close()

def main():
    # If script is executed at the CLI
    usage = '''usage: %(prog)s [-t hostfile] -q -v -vv -vvv'''
    parser = argparse.ArgumentParser(usage=usage)
    parser.add_argument("-t", action="store", dest="targets", default=None, help="Filename for hosts to test")
    parser.add_argument("-v", action="count", dest="verbose", default=1, help="Verbosity level, defaults to one, this outputs each command and result")
    parser.add_argument("-q", action="store_const", dest="verbose", const=0, help="Sets the results to be quiet")
    parser.add_argument('--version', action='version', version='%(prog)s 0.42b')
    args = parser.parse_args()

    # Argument Validator
    if len(sys.argv)==1:
        parser.print_help()
        sys.exit(1)

    if (args.targets == None):
        parser.print_help()
        sys.exit(1)

    # Set Constructors
    verbose = args.verbose   # Verbosity level
    targets = args.targets       # Password or hash to test against default is admin

    host_test(targets)

if __name__ == '__main__':
    main()