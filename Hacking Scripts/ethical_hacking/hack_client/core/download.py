

def downloadFile(my_socket):
    print("[+] Downloading file")
    filename = my_socket.receiveData()

    my_socket.receiveFile(filename)