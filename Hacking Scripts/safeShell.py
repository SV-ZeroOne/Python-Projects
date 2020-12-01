#!/usr/bin/python
#code from https://www.udemy.com/course/offensive-python-mastering-ethical-hacking-using-python/learn/lecture/8095358#overview
# run this code on a linux system by calling python safeShell.py and it will just relay the commands to that shell it was called from without leaving a history

import os


while True:
    command = raw_input("SafeShell@Host >> ")
    os.system(command)
