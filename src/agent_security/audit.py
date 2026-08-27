import hashlib, json
from datetime import datetime, timezone
from pathlib import Path

def write_event(path: str, event: dict) -> dict:
    record={"timestamp":datetime.now(timezone.utc).isoformat(),**event}
    canonical=json.dumps(record,sort_keys=True,separators=(",",":"))
    record["event_hash"]=hashlib.sha256(canonical.encode()).hexdigest()
    with Path(path).open("a",encoding="utf-8") as f: f.write(json.dumps(record)+"\n")
    return record

