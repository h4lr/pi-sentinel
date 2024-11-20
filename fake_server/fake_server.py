import http.server
import socketserver
import logging

# Define the port number
PORT = 8080

# Create a request handler
class RequestHandler(http.server.SimpleHTTPRequestHandler):
    def do_GET(self):
        # GET request log
        logging.info(f"Received GET request from {self.client_address}")
        # Respond with a 200 OK 
        self.send_response(200)
        self.send_header("Content-type", "text/html")
        self.end_headers()
        self.wfile.write(b"Hello, this is a fake server!")

    def do_POST(self):
        # POST request log
        logging.info(f"Received POST request from {self.client_address}")
        # Respond with a 200 OK 
        self.send_response(200)
        self.send_header("Content-type", "text/html")
        self.end_headers()
        self.wfile.write(b"POST request received")

# Set up logging
logging.basicConfig(filename="server.log", level=logging.INFO)

# Create and start the HTTP server
with socketserver.TCPServer(("", PORT), RequestHandler) as httpd:
    print(f"Fake server running on port {PORT}. Press Ctrl+C to stop.")
    httpd.serve_forever()
