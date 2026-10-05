import json
from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer
from pathlib import Path
from urllib.error import HTTPError, URLError
from urllib.request import Request, urlopen


ROOT = Path(__file__).resolve().parent
MODEL_URL = "http://127.0.0.1:8000/invocations"


class Handler(BaseHTTPRequestHandler):
    def do_GET(self):
        if self.path not in ("/", "/interface.html"):
            self.send_error(404)
            return

        page = (ROOT / "interface.html").read_bytes()
        self.send_response(200)
        self.send_header("Content-Type", "text/html; charset=utf-8")
        self.send_header("Content-Length", str(len(page)))
        self.end_headers()
        self.wfile.write(page)

    def do_POST(self):
        if self.path != "/api/predict":
            self.send_error(404)
            return

        try:
            length = int(self.headers.get("Content-Length", "0"))
            payload = self.rfile.read(length)
            request = Request(
                MODEL_URL,
                data=payload,
                headers={"Content-Type": "application/json"},
                method="POST",
            )
            with urlopen(request, timeout=30) as response:
                body = response.read()
                self.send_response(response.status)
        except HTTPError as error:
            body = json.dumps({"error": error.read().decode("utf-8", "replace")}).encode()
            self.send_response(error.code)
        except (URLError, TimeoutError, ValueError) as error:
            body = json.dumps({"error": f"Serveur MLflow indisponible : {error}"}).encode()
            self.send_response(503)

        self.send_header("Content-Type", "application/json; charset=utf-8")
        self.send_header("Content-Length", str(len(body)))
        self.end_headers()
        self.wfile.write(body)

    def log_message(self, format_string, *args):
        print(f"{self.address_string()} - {format_string % args}")


if __name__ == "__main__":
    server = ThreadingHTTPServer(("127.0.0.1", 8080), Handler)
    print("Interface disponible sur http://127.0.0.1:8080")
    server.serve_forever()