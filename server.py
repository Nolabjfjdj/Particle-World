from http.server import SimpleHTTPRequestHandler, ThreadingHTTPServer
from pathlib import Path
import os

ROOT = Path(__file__).resolve().parent
os.chdir(ROOT)

class ParticleWorldHandler(SimpleHTTPRequestHandler):
    extensions_map = {
        **SimpleHTTPRequestHandler.extensions_map,
        ".js": "application/javascript",
        ".css": "text/css",
    }

if __name__ == "__main__":
    address = ("0.0.0.0", int(os.environ.get("PORT", "8000")))
    print(f"Particle World disponible sur http://localhost:{address[1]}")
    ThreadingHTTPServer(address, ParticleWorldHandler).serve_forever()