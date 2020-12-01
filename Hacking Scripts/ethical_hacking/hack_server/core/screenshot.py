

def captureScreenshot(my_socket):
    print("[+] Capturing screenshot")
    zipped_name = "screenshot.zip"
    my_socket.receiveZipped(zipped_name)     