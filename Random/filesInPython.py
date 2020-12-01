#Files in python
'''
Python uses file objects to interact with external files on your computer. 
These file objects can be any sort of file you have on your computer, whether it be an audio file, a text file, emails, Excel documents, etc. 
Note: You will probably need to install certain libraries or modules to interact with those various file types, but they are easily available.
'''

myfile = open('myTestFile.txt')
print(myfile.read())
#set the read cursor back to the begining for the file
myfile.seek(0)

'''
For Windows you need to use double \ so python doesn't treat the second \ as an escape character, a file path is in the form:

myfile = open("C:\\Users\\YourUserName\\Home\\Folder\\myfile.txt")
For MacOS and Linux you use slashes in the opposite direction:

myfile = open("/Users/YouUserName/Folder/myfile.txt")
'''

print('Its a good practice to close your files')
myfile.close()

#this will automatically close the file.
fileModes = '''
File modes: 
r - read 
w - write (will overwrite for create new files)
a - append (will add to files)
r+ - reading and writing
w+ - writing and reading (Overwrite existing files or creates a new file!)
'''
print(fileModes)
with open('myTestFile.txt', mode = 'a') as my_new_file:
    my_new_file.write('\nmore random text')
    
with open('myTestFile.txt', mode = 'r') as my_new_file:
    print(my_new_file.read())