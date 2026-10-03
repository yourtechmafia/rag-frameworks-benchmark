"""Minimal OpenAI-compatible /v1/embeddings server for BAAI/bge-small-en-v1.5.

GraphRAG only talks to embedding providers through LiteLLM, so this lets it use
the same local embedding model as every other pipeline. Standard library only,
plus sentence-transformers. Run inside the baseline venv:
    python scripts/embed_server.py 8790
"""
import json
import sys
from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer
from threading import Lock

from sentence_transformers import SentenceTransformer

MODEL = SentenceTransformer("BAAI/bge-small-en-v1.5", device="cpu")
LOCK = Lock()


class Handler(BaseHTTPRequestHandler):
    def do_POST(self):
        body = json.loads(self.rfile.read(int(self.headers["Content-Length"])))
        texts = body["input"] if isinstance(body["input"], list) else [body["input"]]
        with LOCK:
            vectors = MODEL.encode(texts, batch_size=32).tolist()
        out = {
            "object": "list",
            "model": body.get("model", "bge-small-en-v1.5"),
            "data": [{"object": "embedding", "index": i, "embedding": v} for i, v in enumerate(vectors)],
            "usage": {"prompt_tokens": 0, "total_tokens": 0},
        }
        data = json.dumps(out).encode()
        self.send_response(200)
        self.send_header("Content-Type", "application/json")
        self.send_header("Content-Length", str(len(data)))
        self.end_headers()
        self.wfile.write(data)

    def log_message(self, *args):
        pass


if __name__ == "__main__":
    port = int(sys.argv[1]) if len(sys.argv) > 1 else 8790
    ThreadingHTTPServer(("127.0.0.1", port), Handler).serve_forever()
