import json
import re

def fix_cors():
    # 1. Update vercel.json
    with open("vercel.json", "r", encoding="utf-8") as f:
        config = json.load(f)
    
    # Check if proxy already exists
    has_api = False
    for r in config.get("rewrites", []):
        if r.get("source") == "/api/shorten":
            has_api = True
            
    if not has_api:
        config["rewrites"].insert(0, {
            "source": "/api/shorten",
            "destination": "https://steep-glade-3331.bhindersingh199529.workers.dev/"
        })
        with open("vercel.json", "w", encoding="utf-8") as f:
            json.dump(config, f, indent=4)
            
    # 2. Update HTML
    with open("free-url-shortener-online.html", "r", encoding="utf-8") as f:
        content = f.read()
        
    content = content.replace(
        "fetch('https://steep-glade-3331.bhindersingh199529.workers.dev/',",
        "fetch('/api/shorten',"
    )
    
    # 3. Create intelligent local server proxy
    server_code = """
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
"""
    with open("scratch/local_server.py", "w", encoding="utf-8") as f:
        f.write(server_code.strip())

if __name__ == "__main__":
    fix_cors()
