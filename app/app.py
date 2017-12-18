import os
import http.server
import socketserver
from time import sleep


PORT = os.environ.get('APP_PORT', 8000)
NAME = os.environ.get('NAME', 'Unknown')
print("starting...")
sleep(3)

class Handler(http.server.SimpleHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header('Content-type', 'text/plain')
        self.end_headers()
        self.wfile.write(('App: ' + NAME).encode())

with socketserver.TCPServer(("", PORT), Handler) as httpd:
    print("ready serving at port", PORT)
    httpd.serve_forever()