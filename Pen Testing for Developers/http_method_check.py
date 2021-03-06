import requests
# This script is a good base script to check the web servers response to different HTTP methods.
# Currently it is checking for Cross Site Tracing (XST) attacks

verbs = ['GET', 'POST', 'PUT', 'DELETE', 'OPTIONS', 'TRACE','TEST']

for verb in verbs:
    req = requests.request(verb, 'http://packtpub.com')
    print verb, req.status_code, req.reason
    if verb == 'TRACE' and 'TRACE / HTTP/1.1' in req.text:
        print 'Possible Cross Site Tracing vulnerability found'