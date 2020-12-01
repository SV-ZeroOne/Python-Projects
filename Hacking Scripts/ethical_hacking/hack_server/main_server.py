from core.connection import ServerConnection
from core.handleConnection import handleConnection

if __name__ == "__main__":
    my_socket = ServerConnection()
    my_socket.createConnection("192.168.1.33", 9001)
    my_socket.listen()
    #my_conn, client_add = my_socket.acceptConnection()
    #my_socket.sendData("Hi this is the server.")
    #print(my_socket.receiveData())
    my_conn, _ = my_socket.acceptConnection()
    handleConnection(my_socket)
    my_conn.close()