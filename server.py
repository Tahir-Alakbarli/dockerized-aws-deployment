import json
from http.server import SimpleHTTPRequestHandler, ThreadingHTTPServer
from pathlib import Path


FRONTEND_DIRECTORY = Path(__file__).parent / "frontend"


class WebsiteHandler(SimpleHTTPRequestHandler):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, directory=str(FRONTEND_DIRECTORY), **kwargs)

    def do_GET(self):
        if self.path == "/health":
            response = json.dumps({"status": "healthy"}).encode("utf-8")
            self.send_response(200)
            self.send_header("Content-Type", "application/json")
            self.send_header("Content-Length", str(len(response)))
            self.end_headers()
            self.wfile.write(response)
            return

        super().do_GET()


server = ThreadingHTTPServer(("0.0.0.0", 8000), WebsiteHandler)
print("Website running on port 8000")
server.serve_forever()
