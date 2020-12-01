from glob import glob
import os

# read file from the disk on hacker machine
# read it in the form of bytes
# append a delimeter to the end of bytes
# transfer file over the network
# remove the delimeter from the bytes to recover the original data
# write the file to the client disk


def uploadFiles(my_socket):
    print("[+] Executing uploadFiles function")
    # Will search current directory for all files
    files = glob("*")
    for index, filename in enumerate(files):
        new_filename = os.path.basename(filename)
        print("\t\t", index, "\t", new_filename)
    
    while True:
        try:
            file_index = int(input("[+] Select file : "))
            if len(files) >= file_index >= 0:
                fileName = files[file_index]
                break
        except:
            print("[!] Invalid file selected")

    print("[+] Select file : ", fileName)
    my_socket.sendData(fileName)
    my_socket.sendFile(fileName)