#!/usr/bin/env python

import scanner


#target_url = "http://10.0.2.4/mutillidae/"
target_url = "http://10.0.2.4/dvwa/"
links_to_ignore = ["http://10.0.2.4/dvwa/logout.php"]

data_dict = {"username": "admin", "password": "password", "Login": "submit"}

vuln_scanner = scanner.Scanner(target_url, links_to_ignore)
vuln_scanner.session.post("http://10.0.2.4/dvwa/login.php", data=data_dict)

vuln_scanner.crawl()
vuln_scanner.run_scanner()