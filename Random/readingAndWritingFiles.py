import sys
import os

print('#'*100)
print('Reading and Writing Files')
print('''\
r - read
w - write
a - append''')
print('#'*100)
path = os.path.dirname(__file__)
print("Current working path is {}".format(path))
file = open('B:/Python-Projects/Random/TestFiles/testFile.json', 'a')
print('Opened testFile.json')
file.write('{ "new": "object" }')
#close makes sure that the file doesnt stay in the buffer.
file.close()

