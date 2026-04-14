import http.server
import socketserver
import os
import urllib.request
import json

PORT = 3000

class CustomHandler(http.server.SimpleHTTPRequestHandler):
    def do_POST(self):
        if self.path == '/api/shorten':
            content_length = int(self.headers['Content-Length'])
            post_data = self.rfile.read(content_length)
            
            # Proxy directly to worker
            req = urllib.request.Request(
                'https://steep-glade-3331.bhindersingh199529.workers.dev/', 
                data=post_data,
                headers={'Content-Type': 'application/json'}
            )
            
            try:
                response = urllib.request.urlopen(req)
                resp_data = response.read()
                
                self.send_response(200)
                self.send_header('Content-type', 'application/json')
                self.end_headers()
                self.wfile.write(resp_data)
            except Exception as e:
                print("Proxy Error:", e)
                self.send_response(500)
                self.end_headers()
            return
            
        self.send_response(404)
        self.end_headers()

    def do_GET(self):
        # Handle cleanUrls similar to Vercel
        if not self.path.endswith('/') and '.' not in self.path:
            path_no_query = self.path.split('?')[0]
            html_path = "." + path_no_query + ".html"
            if os.path.exists(html_path):
                self.path = self.path.replace(path_no_query, path_no_query + ".html")
        return super().do_GET()

with socketserver.TCPServer(("", PORT), CustomHandler) as httpd:
    httpd.allow_reuse_address = True
    print(f"Serving at port {PORT} with Vercel API Proxy enabled")
    httpd.serve_forever()
