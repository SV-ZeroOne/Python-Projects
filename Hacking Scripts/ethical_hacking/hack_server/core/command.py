

def runCommand(my_socket):
    print("[+] Running commands")
    while True:
        command = input(">> ")

        my_socket.sendData(command)

        if command == "":
            continue

        if command == "stop":
            break

        result = my_socket.receiveCommandResult()
        print(result)
