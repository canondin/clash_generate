import http.server
import socketserver

PORT = 8081

Handler = http.server.SimpleHTTPRequestHandler

with socketserver.TCPServer(("", PORT), Handler) as httpd:
    print("Server started at localhost:{}".format(PORT))
    httpd.serve_forever()
