'''
Caution: Using this script for any malicious purpose is prohibited and against the law. Please read Twitter terms and conditions carefully. Use it on your own risk. 
'''


# Python For Offensive PenTest: A Complete Practical Course - All rights reserved 
# Follow me on LinkedIn  https://jo.linkedin.com/in/python2



from bs4 import BeautifulSoup as soupy
import urllib.request
import re


#Navigate to my twitter home page HussamKhrais, store the HTML page into html variable and pass it
#to soupy function so we can parse it

html = urllib.request.urlopen('https://twitter.com/HussamKhrais').read()
soup = soupy(html, features="html.parser")

#Here we search for specific HTML meta tags
x = soup.find("meta", {"name":"description"})['content']


filter = re.findall(r'"(.*)"', x) # filter any character between the double quotes and add that to a capture group.
tweet = filter[0]  


print(tweet)
