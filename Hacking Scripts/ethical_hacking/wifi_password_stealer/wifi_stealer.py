#!/usr/bin/python3
# Gather stored wifi passwords on windows
import subprocess

# netsh wlan show profiles

completed_process = subprocess.run(["netsh", "wlan","show", "profiles"], shell=True, capture_output=True)
output = completed_process.stdout.decode()
print(output)
output = output.split("\n")

access_points = []
for line in output:
    if "All User Profile" in line:
        split_line = line.split(":")
        #Strip the front space and the last newline
        ap = split_line[1][1:-1]
        access_points.append(ap)


# netsh wlan show profile apName key=clear
for ap in access_points:
    ap_result = subprocess.run(["netsh", "wlan","show", "profiles", ap, "key=clear"], shell=True, capture_output=True)
    ap_result = ap_result.stdout.decode()
    ap_result_list = ap_result.split("\n")
    for line_result in ap_result_list:
        if "SSID name" in line_result:
            print(line_result)

        if "Key Content" in line_result:
            print(line_result)