import json
import sys
import traceback

def log(message: str):
    sys.stderr.write(f"[simple-mcp] {message}\n")
    sys.stderr.flush()
    with open("/tmp/simple-mcp.log", "a") as f:
        f.write(f"[simple-mcp] {message}\n")

def send(obj):
    s = json.dumps(obj, ensure_ascii=False)
    log(f"-> {s}")
    sys.stdout.write(s + "\n")
    sys.stdout.flush()

def send_error(req_id, code, message, data=None):
    err = {"code": code, "message": message}
    if data is not None:
        err["data"] = data
    send({"jsonrpc": "2.0", "id": req_id, "error": err})

def main():
    log("Server started, waiting for stdin JSON-RPC...")

    while True:
        line = sys.stdin.readline()
        if not line:
            log("stdin closed, exiting.")
            return

        line = line.strip()
        if not line:
            continue

        log(f"<- {line}")

        req_id = None
        try:
            req = json.loads(line)
            req_id = req.get("id")
            method = req.get("method")
            params = req.get("params") or {}

            # ---- Handshake ----
            if method == "initialize":
                send({
                    "jsonrpc": "2.0",
                    "id": req_id,
                    "result": {
                        "protocolVersion": "2024-11-05",
                        "capabilities": {
                            "tools": {
                                "listChanged": False
                            }
                        },
                        "serverInfo": {"name": "PurePythonDemo", "version": "1.0.0"}
                    }
                })
                continue

            if method == "notifications/initialized":
                # Notification has no id
                log("Client sent notifications/initialized")
                continue

            # ---- Tools ----
            if method == "tools/list":
                send({
                    "jsonrpc": "2.0",
                    "id": req_id,
                    "result": {
                        "tools": [
                            {
                                "name": "get_system_info",
                                "description": "Returns basic system info",
                                "inputSchema": {
                                    "type": "object",
                                    "properties": {},
                                    "additionalProperties": False
                                }
                            }
                        ]
                    }
                })
                continue

            if method == "tools/call":
                name = params.get("name")
                arguments = params.get("arguments") or {}

                if name == "get_system_info":
                    send({
                        "jsonrpc": "2.0",
                        "id": req_id,
                        "result": {
                            "content": [
                                {"type": "text", "text": "Hello! Python: " + sys.version}
                            ]
                        }
                    })
                else:
                    send_error(req_id, -32602, f"Unknown tool: {name}", {"knownTools": ["get_system_info"]})
                continue

            # ---- Anything else: answer method-not-found (super helpful for debugging) ----
            send_error(req_id, -32601, f"Method not found: {method}")

        except json.JSONDecodeError as e:
            # If it wasn't valid JSON we can't reliably respond with an id
            log(f"JSON decode error: {e}")
        except Exception as e:
            tb = traceback.format_exc()
            log(f"Unhandled error: {e}\n{tb}")
            send_error(req_id, -32603, str(e), {"traceback": tb})

if __name__ == "__main__":
    main()