#This script is used to check for server time jitter.

import requests
import sys


input = sys.argv[1]
def averagetimer(url):
    i = 0
    values = []
    while i < 100:
        r = requests.get(url)
        values.append(int(r.elapsed.total_seconds()))
        i = i + 1

    average = sum(values) / float(len(values))
    return average


averagetimer(input)