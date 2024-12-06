import http.server
import socketserver
import os

class CustomHttpRequestHandler(http.server.SimpleHTTPRequestHandler):
    def do_GET(self):
        if self.path == '/':
            self.path = 'index.html'
        return http.server.SimpleHTTPRequestHandler.do_GET(self)
os.chdir(r"C:\Users\aiden\OneDrive\Desktop\Coding\Coding_Project\Hovren_Security_Solutions\templates")
PORT = 5500

handler = CustomHttpRequestHandler
server=socketserver.TCPServer(("", PORT), handler)
print("Server started at port 5500. Press CTRL+C to close the server.")
try:
	server.serve_forever()
except KeyboardInterrupt:
	server.server_close()
	print("Server Closed")