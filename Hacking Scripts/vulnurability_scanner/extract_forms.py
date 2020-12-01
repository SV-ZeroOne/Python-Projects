#!/usr/bin/env python
# Had to install the library below with C:/Python27/Scripts/pip.exe install BeautifulSoup


import requests
from BeautifulSoup import BeautifulSoup
import urlparse


def request(url):
    try:
        return requests.get(url)
    except requests.exceptions.ConnectionError:
        pass


target_url = "http://10.0.2.4/mutillidae/index.php?page=dns-lookup.php"
response = request(target_url)

#print(response.content)

parsed_html = BeautifulSoup(response.content)
forms_list = parsed_html.findAll("form")
#print(forms_list)

for form in forms_list:
    action = form.get("action")
    #will have to add check to see if the action contains full URL or partial URL
    post_url = urlparse.urljoin(target_url, action)
    #print(action)
    method = form.get("method")
    #print(method)

    inputs_list = form.findAll("input")
    post_data = {}
    for some_input in inputs_list:
        input_name = some_input.get("name")
        #print(input_name)
        input_type = some_input.get("type")
        input_value = some_input.get("value")
        if input_type == "text":
            input_value = "test"

        post_data[input_name] = input_value
    result = requests.post(post_url, data=post_data)
    print(result.content)




