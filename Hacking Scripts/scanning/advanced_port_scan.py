#!/usr/bin/python

from socket import *
import optparse
from threading import *


def connectionScan(tgtHost, tgtPort):
    try:
        sock = socket(AF_INET, SOCK_STREAM)
        sock.connect((tgtHost,tgtPort))
        print '[+] %d/tcp Open' %tgtPort
    except:
        print '[-] %d/tcp Closed\n' %tgtPort
    finally:
        sock.close()


def portScan(tgtHost, tgtPorts):
    try:
        tgtIp = gethostbyname(tgtHost)
    except:
        print 'Cant Resolve Target Host IP: %s' %tgtHost
    try:
        tgtName = gethostbyaddr(tgtIp)
        print '[+] Scan Results for: '+ tgtName[0]
    except:
        print '[+] Scan Results for: ' + tgtIp
    setdefaulttimeout(1)
    for tgtPort in tgtPorts:
        t = Thread(target=connectionScan, args=(tgtHost, int(tgtPort)))
        t.start()


def main():
    parser = optparse.OptionParser('Usage of program: ' + '-H <target host> -p <target ports>')
    parser.add_option('-H', dest='tgtHost', type='string', help='specify target host')
    parser.add_option('-p', dest='tgtPort', type='string', help='specify target ports seperated by comma')
    (options, args) = parser.parse_args()
    tgtHost = options.tgtHost
    tgtPorts = str(options.tgtPort).split(',')
    if (tgtHost == None) | (tgtPorts[0] == None):
        print parser.usage
        exit(0)
    portScan(tgtHost,tgtPorts)


if __name__ == '__main__':
    main()