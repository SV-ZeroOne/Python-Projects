import requests
'''
The next part of the HTTP protocol that we will be concentrating on are the HTTP headers.
Found in both the requests and responses from the web server, these carry extra information
between the client and server. Any area with extra data makes a great place to parse
information about the servers and to look for potential issues.
'''


req = requests.get('http://packtpub.com')
headers = ['Server', 'Date', 'Via', 'X-Powered-By', 'X-Country-Code']
for header in headers:
    try:
        result = req.headers[header]
        print '%s: %s' % (header, result)
    except Exception, error:
        print '%s: Not found' % header