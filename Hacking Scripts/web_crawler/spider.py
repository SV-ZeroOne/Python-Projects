#!/usr/bin/env python
import requests, os
import re
import urlparse

target_url = "https://test.com"
target_links = []

def extract_links_from(url):
    response = requests.get(url)
    #re seems to only work with python2
    return re.findall('(?:href=")(.*?)"', response.content)

def crawl(url):    
    href_links = extract_links_from(url)
    for link in href_links:
        #convert relative links to full links
        link = urlparse.urljoin(url, link)
        if "#" in link:
            link = link.split("#")[0]
        
        #only show links for the target website and not external links
        if target_url in link and link not in target_links:
            target_links.append(link)
            print(link)
            #recursive method
            crawl(link)


crawl(target_url)