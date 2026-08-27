from functools import lru_cache
from pathlib import Path
import os, yaml

ROOT = Path(__file__).resolve().parents[2]

@lru_cache
def load_yaml(name: str) -> dict:
    return yaml.safe_load((ROOT / "config" / name).read_text(encoding="utf-8"))

def settings() -> dict:
    return {
        "auth_mode": os.getenv("AUTH_MODE", "mock"),
        "issuer": os.getenv("PING_ISSUER", "https://auth.example.com"),
        "audience": os.getenv("PING_AUDIENCE", "agent-security-api"),
        "jwks_url": os.getenv("PING_JWKS_URL", "https://auth.example.com/.well-known/jwks.json"),
        "introspection_url": os.getenv("PING_INTROSPECTION_URL", ""),
        "client_id": os.getenv("PING_CLIENT_ID", ""),
        "client_secret": os.getenv("PING_CLIENT_SECRET", ""),
        "audit_log_path": os.getenv("AUDIT_LOG_PATH", "audit.log"),
    }

