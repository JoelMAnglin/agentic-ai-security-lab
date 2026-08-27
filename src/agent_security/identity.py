import base64, json
import httpx, jwt
from jwt import PyJWKClient
from .models import Principal

def _scopes(value) -> set[str]:
    if isinstance(value, str): return set(value.split())
    if isinstance(value, list): return set(value)
    return set()

def validate_mock_token(token: str) -> Principal:
    """Decode a safe lab token: base64url(JSON), never use this in production."""
    try:
        raw = base64.urlsafe_b64decode(token + "=" * (-len(token) % 4))
        claims = json.loads(raw)
        return Principal(subject=claims["sub"], scopes=_scopes(claims.get("scope", "")))
    except Exception as exc:
        raise ValueError("invalid mock token") from exc

def validate_jwt(token: str, issuer: str, audience: str, jwks_url: str) -> Principal:
    key = PyJWKClient(jwks_url).get_signing_key_from_jwt(token).key
    claims = jwt.decode(token, key, algorithms=["RS256", "ES256"], issuer=issuer, audience=audience)
    return Principal(subject=claims.get("sub") or claims["client_id"], scopes=_scopes(claims.get("scope")), issuer=claims["iss"])

def introspect(token: str, url: str, client_id: str, client_secret: str) -> Principal:
    response = httpx.post(url, data={"token": token}, auth=(client_id, client_secret), timeout=5)
    response.raise_for_status(); claims = response.json()
    if not claims.get("active"): raise ValueError("inactive token")
    return Principal(subject=claims.get("sub") or claims["client_id"], scopes=_scopes(claims.get("scope")), issuer=claims.get("iss", "introspection"))

def validate_token(token: str, cfg: dict) -> Principal:
    if cfg["auth_mode"] == "mock": return validate_mock_token(token)
    if cfg["auth_mode"] == "introspection": return introspect(token, cfg["introspection_url"], cfg["client_id"], cfg["client_secret"])
    if cfg["auth_mode"] == "jwt": return validate_jwt(token, cfg["issuer"], cfg["audience"], cfg["jwks_url"])
    raise ValueError("unsupported AUTH_MODE")

