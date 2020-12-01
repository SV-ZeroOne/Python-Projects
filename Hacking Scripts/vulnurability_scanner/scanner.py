#!/usr/bin/env python

import requests
import re
import urlparse
from BeautifulSoup import BeautifulSoup


class Scanner:
    def __init__(self, url, ignore_links):
        self.session = requests.Session()
        self.target_url = url
        self.target_links = []
        self.links_to_ignore = ignore_links

    def extract_links_from(self, url):
        response = self.session.get(url)
        #re seems to only work with python2
        return re.findall('(?:href=")(.*?)"', response.content)

    #default value of None
    def crawl(self, url=None):
        if url == None:
            url = self.target_url    
        href_links = self.extract_links_from(url)
        for link in href_links:
            #convert relative links to full links
            link = urlparse.urljoin(url, link)
            if "#" in link:
                link = link.split("#")[0]
            
            #only show links for the target website and not external links
            if self.target_url in link and link not in self.target_links and link not in self.links_to_ignore:
                self.target_links.append(link)
                print(link)
                #recursive method
                self.crawl(link)

    def extract_forms(self, url):
        response = self.session.get(url)
        parsed_html = BeautifulSoup(response.content)
        return parsed_html.findAll("form")

    def submit_form(self, form, value, url):
        action = form.get("action")
        #will have to add check to see if the action contains full URL or partial URL
        post_url = urlparse.urljoin(url, action)
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
                input_value = value

            post_data[input_name] = input_value
        if method == "post"
            return self.session.post(post_url, data=post_data)
        return self.session.get(post_url, params=post_data)

    def run_scanner(self):
        for link in self.target_links:
            forms = self.extract_forms(link)
            for form in forms:
                print("[+] Testing form in " + link)
                is_vulnerable_to_xss = self.test_xss_in_form(form, link)
                if is_vulnerable_to_xss:
                    print("\n\n[***] XSS discovered in " + link + " in the following form")
                    print(form)
            
            if "=" in link:
                print("\n\n[+] Testing " + link)
                is_vulnerable_to_xss = self.test_xss_in_link(link)
                if is_vulnerable_to_xss:
                    print("[***] XSS discovered in " + link)

    def test_xss_in_form(self, form, url):
        #made the script tag with random caps to bypass simple filtering
        xss_test_script = "<sCript>alert('test')</scriPt>"
        response = self.submit_form(form, xss_test_script, url)
        #returns true or false
        return xss_test_script in response.content

    def test_xss_in_link(self, url):
        xss_test_script = "<sCript>alert('test')</scriPt>"
        url = url.replace("=", "=" + xss_test_script)
        response = self.session.get(url)
        return xss_test_script in response.content
