# 3 - Connect PingFederate or PingOne

This lab supports two production-style validation paths: signed JWT validation through OIDC/JWKS and OAuth token introspection. Exact console labels vary by Ping product/version, so use your tenant documentation as the final authority.

## Architecture

1. Register a confidential OAuth client for the agent.
2. Use client credentials for a non-human workload.
3. Issue only required scopes, such as `agent:run ticket:read`.
4. Configure the API audience `agent-security-api`.
5. Validate issuer, audience, signature, expiry, and scope at the gateway.
6. Map token subject/client ID to the same `agent_id` in `agents.yaml`.

## Option A: JWT and JWKS

Set:

```env
AUTH_MODE=jwt
PING_ISSUER=https://YOUR-PING-ISSUER
PING_AUDIENCE=agent-security-api
PING_JWKS_URL=https://YOUR-PING-ISSUER/.well-known/jwks.json
```

The gateway accepts only RS256 or ES256 tokens and checks issuer and audience. Do not disable these checks to “make it work.”

## Option B: introspection

Set:

```env
AUTH_MODE=introspection
PING_INTROSPECTION_URL=https://YOUR-PING-HOST/as/introspect.oauth2
PING_CLIENT_ID=YOUR-API-CLIENT
PING_CLIENT_SECRET=STORE-THIS-IN-A-SECRET-MANAGER
```

The gateway requires `active=true`. Introspection adds a network dependency; use short timeouts and fail closed.

## Ping configuration checklist

- [ ] Agent client is confidential and uniquely named
- [ ] Client credentials grant is allowed only where appropriate
- [ ] Token lifetime is short
- [ ] Audience is restricted to this API
- [ ] Scopes are minimal and tool-specific
- [ ] Client secret is not in Git or `.env.example`
- [ ] Rotation owner and expiry are documented
- [ ] Token subject/client ID matches the registered agent
- [ ] Revocation/introspection behavior is tested
- [ ] Authentication failures reach the SIEM

## Tests to capture for a portfolio

1. Valid token and scope -> allow
2. Expired token -> 401
3. Wrong issuer -> 401
4. Wrong audience -> 401
5. Missing scope -> deny
6. Revoked/inactive token -> 401
7. Token for agent A used by agent B -> deny

Redact tokens and secrets from screenshots.

