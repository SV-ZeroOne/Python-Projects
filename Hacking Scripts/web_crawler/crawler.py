#!/usr/bin/env python
import requests, os

def request(url):
    try:
        return requests.get("http://" + url)
    except requests.exceptions.ConnectionError:
        pass

dirpath = os.getcwd()
print("current directory is : " + dirpath)

target_url = "10.0.2.7/mutillidae"
with open(dirpath + "/subdomains-wordlist.txt", "r") as wordlist_file:
    for line in wordlist_file:
        word = line.strip()
        test_url = word + "." + target_url
        #print(test_url)
        response = request(test_url)
        if response:
            print("[+] Discovered subdomain -->" + test_url)
            #can store the subdomain in a db or list

'''
# This is for finding sub directories for a website.
with open(dirpath + "/files-and-dirs-wordlist.txt", "r") as wordlist_file:
    for line in wordlist_file:
        word = line.strip()
        test_url = target_url + "/" + word
        #print(test_url)
        response = request(test_url)
        if response:
            print("[+] Discovered subdomain -->" + test_url)
            #can store the subdomain in a db or list
            #can add another loop to look for sub-sub directories
'''