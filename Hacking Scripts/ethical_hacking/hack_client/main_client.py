from core.connection import ClientConnection
from core.handleConnection import handleConnection


if __name__ == "__main__":
    print("[+] Establishing connection with server.")
    my_socket = ClientConnection()
    my_socket.connect("192.168.1.33", 9001)
    handleConnection(my_socket)
    #print(my_socket.receiveData())
    #my_socket.sendData("Hi this is the client")
    my_socket.close()
