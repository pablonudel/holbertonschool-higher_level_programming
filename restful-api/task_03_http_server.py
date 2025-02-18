#!/usr/bin/python3
"""Module for RequestHandler class"""
from http.server import *
import json


class RequestHandler(BaseHTTPRequestHandler):
    """a simple HTTP server"""
    def do_GET(self):
        """method to handle GET requests"""
        if self.path == '/':
            self.send_response(200)
            self.send_header("Content-type", "text")
            self.end_headers()
            data = "Hello, this is a simple API!"
            self.wfile.write(data.encode('utf-8'))
        elif self.path == '/data':
            self.send_response(200)
            self.send_header("Content-type", "application/json")
            self.end_headers()
            data = {"name": "John", "age": 30, "city": "New York"}
            self.wfile.write(json.dumps(data).encode('utf-8'))
        elif self.path == '/status':
            self.send_response(200)
            self.send_header("Content-type", "text")
            self.end_headers()
            self.wfile.write("OK".encode('utf-8'))
        elif self.path == '/info':
            self.send_response(200)
            self.send_header("Content-type", "application/json")
            self.end_headers()
            data = {"version": "1.0",
                    "description": "A simple API built with http.server"}
            self.wfile.write(json.dumps(data).encode('utf-8'))
        else:
            self.send_error(404, "Endpoint not found")
            self.send_header("Content-type", "text")
            self.end_headers()


hostName = 'localhost'
serverPort = 8000

webServer = HTTPServer((hostName, serverPort), RequestHandler)
print("Server started at http://{}:{}".format(hostName, serverPort))
try:
    webServer.serve_forever()
except KeyboardInterrupt:
    pass

webServer.server_close()
print()
print("Server stopped")
