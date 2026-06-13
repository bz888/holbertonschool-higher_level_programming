import json
from http.server import BaseHTTPRequestHandler, HTTPServer


class ApiHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        if self.path == "/":
            self.send_text_response("hello world!")

        elif self.path == "/data":
            self.send_json_response({
                "name": "John",
                "age": 30,
                "city": "New York",
            })

        elif self.path == "/info":
            self.send_json_response({
                "version": "1.0",
                "description": "A simple API built with http.server",
            })

        elif self.path == "/status":
            self.send_json_response({
                "status": "OK",
            })

        else:
            self.send_text_response("Endpoint not found", status_code=404)

    def send_json_response(self, data, status_code=200):
        self.send_response(status_code)
        self.send_header("Content-Type", "application/json")
        self.end_headers()
        self.wfile.write(json.dumps(data).encode("utf-8"))

    def send_text_response(self, message, status_code=200):
        self.send_response(status_code)
        self.send_header("Content-Type", "text/plain")
        self.end_headers()
        self.wfile.write(message.encode("utf-8"))


def run_server():
    server_address = ("", 8000)
    httpd = HTTPServer(server_address, ApiHandler)
    print("Server running at http://localhost:8000")
    httpd.serve_forever()


if __name__ == "__main__":
    run_server()
