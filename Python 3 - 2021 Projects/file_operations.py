'''
Reading and Writing to a .txt file
'''

'''
There is an better way to read file and manage them with a context manager

# r = read only
f = open('test.txt', 'r')
print(f.read())
# Must close, can lead to an memory leak if not closed.
f.close()
'''

# Context Manager will open and close automatically 
with open('test.txt', 'r') as f:
    #print(f.readline())
    print(f.read())
    #print(f.read(100))
    #print(f.tell())
    #print(f.readlines())
    #for line in f:
    #    print(line, end='')


with open('text1.txt', 'w') as f:
    # If the file does not exist it will create it.
    f.write('This is an new file with some text!')
    # If the file does exist it will overwrite whatever is in it.
    f.write('This file was be overwritten')


# reading a photo - rb = read binary
with open('mr_robot.png', 'rb') as photo:
    print(photo.read())
