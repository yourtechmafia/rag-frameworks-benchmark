"""Local pass-through proxy for the Anthropic API that records the real cost of every call.

Every pipeline points ANTHROPIC_BASE_URL (or its framework's equivalent) at this proxy.
It forwards requests to api.anthropic.com unchanged, reads the `usage` block from each
response (streaming or not), prices it, and appends one row per call to ledger/spend.csv.
A hard cap stops all calls once total spend reaches CAP_USD.
"""
import asyncio, csv, json, os, sys, time
from pathlib import Path

import aiohttp
from aiohttp import web

UPSTREAM = "https://api.anthropic.com"
ROOT = Path(__file__).resolve().parents[1]
LEDGER = ROOT / "ledger" / "spend.csv"
PHASE_FILE = Path(os.environ.get("BENCH_PHASE_FILE", Path.home() / "ragbench" / "phase.txt"))
CAP_USD = float(os.environ.get("BENCH_CAP_USD", "75"))
# The benchmark runs every model call at temperature 0. Anthropic's Python SDK 1.x dropped the
# `temperature` keyword (the API still honours it on Haiku 4.5), so integrations differ in whether
# they send it. The proxy sets it on every Messages request so all frameworks run identically.
FORCE_TEMPERATURE = os.environ.get("BENCH_FORCE_TEMPERATURE", "0")

# USD per million tokens: input, output, 5-minute cache write, cache read
PRICES = {
    "claude-haiku-4-5": (1.00, 5.00, 1.25, 0.10),
    "claude-sonnet-4-6": (3.00, 15.00, 3.75, 0.30),
}
FIELDS = ["ts", "phase", "model", "path", "status", "client_temperature", "input_tokens", "output_tokens",
          "cache_creation_input_tokens", "cache_read_input_tokens", "cost_usd", "latency_ms"]


def price_for(model):
    for prefix, p in PRICES.items():
        if model and model.startswith(prefix):
            return p
    return PRICES["claude-sonnet-4-6"]  # unknown model: price conservatively


def total_spend():
    if not LEDGER.exists():
        return 0.0
    with LEDGER.open() as f:
        return sum(float(r["cost_usd"] or 0) for r in csv.DictReader(f))


def record(row):
    new = not LEDGER.exists()
    with LEDGER.open("a", newline="") as f:
        w = csv.DictWriter(f, fieldnames=FIELDS)
        if new:
            w.writeheader()
        w.writerow(row)


def cost(model, u):
    pin, pout, pcw, pcr = price_for(model)
    return (u.get("input_tokens", 0) * pin + u.get("output_tokens", 0) * pout
            + u.get("cache_creation_input_tokens", 0) * pcw
            + u.get("cache_read_input_tokens", 0) * pcr) / 1e6


def phase():
    try:
        return PHASE_FILE.read_text().strip() or "unlabeled"
    except FileNotFoundError:
        return "unlabeled"


async def handle(request: web.Request):
    spent = total_spend()
    if spent >= CAP_USD:
        return web.json_response({"type": "error", "error": {"type": "budget_cap",
                                  "message": f"Bench cap ${CAP_USD} reached (${spent:.2f})"}}, status=429)
    body = await request.read()
    model, client_temp = "", ""
    try:
        payload = json.loads(body) if body else {}
        model = payload.get("model", "")
        client_temp = payload.get("temperature", "")
        if (request.path.startswith("/v1/messages") and not request.path.endswith("count_tokens")
                and FORCE_TEMPERATURE != "" and model.startswith("claude-haiku-4-5")):
            payload["temperature"] = float(FORCE_TEMPERATURE)
            body = json.dumps(payload).encode()
    except ValueError:
        pass
    headers = {k: v for k, v in request.headers.items()
               if k.lower() not in ("host", "content-length", "accept-encoding", "connection", "x-bench-phase")}
    usage, t0 = {}, time.perf_counter()
    session: aiohttp.ClientSession = request.app["session"]
    async with session.request(request.method, UPSTREAM + request.path_qs, data=body, headers=headers) as up:
        ctype = up.headers.get("content-type", "")
        out_headers = {k: v for k, v in up.headers.items()
                       if k.lower() not in ("content-length", "content-encoding", "transfer-encoding", "connection")}
        if "text/event-stream" in ctype:
            resp = web.StreamResponse(status=up.status, headers=out_headers)
            await resp.prepare(request)
            buf = b""
            async for chunk in up.content.iter_any():
                await resp.write(chunk)
                buf += chunk
                while b"\n" in buf:
                    line, buf = buf.split(b"\n", 1)
                    if line.startswith(b"data:"):
                        try:
                            ev = json.loads(line[5:].strip())
                        except ValueError:
                            continue
                        u = (ev.get("message") or {}).get("usage") or ev.get("usage") or {}
                        for k, v in u.items():
                            if isinstance(v, int):
                                usage[k] = max(usage.get(k, 0), v)
            await resp.write_eof()
        else:
            data = await up.read()
            resp = web.Response(status=up.status, body=data, headers=out_headers)
            try:
                usage = json.loads(data).get("usage") or {}
            except ValueError:
                usage = {}
    if request.path.startswith("/v1/messages") and not request.path.endswith("count_tokens"):
        record({"ts": time.strftime("%Y-%m-%dT%H:%M:%S"), "phase": request.headers.get("x-bench-phase") or phase(), "model": model,
                "path": request.path, "status": up.status, "client_temperature": client_temp,
                "input_tokens": usage.get("input_tokens", 0), "output_tokens": usage.get("output_tokens", 0),
                "cache_creation_input_tokens": usage.get("cache_creation_input_tokens", 0),
                "cache_read_input_tokens": usage.get("cache_read_input_tokens", 0),
                "cost_usd": f"{cost(model, usage):.6f}",
                "latency_ms": int((time.perf_counter() - t0) * 1000)})
    return resp


async def on_startup(app):
    app["session"] = aiohttp.ClientSession(timeout=aiohttp.ClientTimeout(total=600))


async def on_cleanup(app):
    await app["session"].close()


def main():
    port = int(sys.argv[1]) if len(sys.argv) > 1 else 8787
    app = web.Application(client_max_size=50 * 1024 * 1024)
    app.on_startup.append(on_startup)
    app.on_cleanup.append(on_cleanup)
    app.router.add_route("*", "/{tail:.*}", handle)
    web.run_app(app, host="127.0.0.1", port=port, print=None)


if __name__ == "__main__":
    main()
