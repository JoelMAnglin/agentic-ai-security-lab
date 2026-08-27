# Agentic AI Security Lab: Ping Identity, Bot Guardrails, and NHI Governance

[![CI](https://github.com/JoelMAnglin/agentic-ai-security-lab/actions/workflows/ci.yml/badge.svg)](https://github.com/JoelMAnglin/agentic-ai-security-lab/actions/workflows/ci.yml)

A beginner-friendly, defensive lab for learning how to secure AI agents ("bots") that call enterprise tools. It demonstrates Ping-compatible OAuth/OIDC identity, non-human identity (NHI) governance, least privilege, human approval for risky actions, prompt-injection defenses, immutable-style audit events, a kill switch, and repeatable policy tuning.

The design is **CISSP-aligned**, using security-domain principles such as least privilege, separation of duties, defense in depth, secure defaults, auditability, and incident response. It does not claim that the author holds the CISSP certification.

> Safe lab: the included agent uses local deterministic logic. It does not attack external systems, collect secrets, or require a paid LLM/API.

## What you will build

```text
Human owner -> Ping-compatible token -> Agent gateway -> Policy engine -> Tool
                                      |       |             |
                                      |       |             +-- deny / allow / require approval
                                      |       +-- prompt-injection and data-loss checks
                                      +-- audit trail, risk score, kill switch
```

The project mirrors current industry patterns:

- **Oasis-style controls:** inventory agent identities, discover permissions, enforce least privilege, govern lifecycle, and retain a human-to-agent-to-action audit chain.
- **HYPR AgentPass-style controls:** give each agent verifiable identity, enforce policy inline, require human supervision for high-risk actions, and support immediate termination.
- **Ping experience:** validate JWTs through OIDC/JWKS or OAuth introspection, enforce scopes/audience/issuer, and model client-credentials access for a non-human agent.

## Beginner quick start

### 1. Install prerequisites

- Git
- Python 3.11 or newer
- Optional: Docker Desktop

### 2. Clone and enter the project

```bash
git clone https://github.com/JoelMAnglin/agentic-ai-security-lab.git
cd agentic-ai-security-lab
```

### 3. Create a virtual environment

Windows PowerShell:

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
python -m pip install --upgrade pip
pip install -r requirements.txt
```

macOS/Linux:

```bash
python3 -m venv .venv
source .venv/bin/activate
python -m pip install --upgrade pip
pip install -r requirements.txt
```

### 4. Run the tests

```bash
pytest -q
```

### 5. Start the API

```bash
uvicorn agent_security.api:app --app-dir src --reload
```

Open `http://127.0.0.1:8000/docs`.

### 6. Try the safe demo

In another terminal:

```bash
python scripts/demo.py
```

You will see:

1. a low-risk read action allowed;
2. a sensitive write routed to human approval;
3. a prompt-injection attempt denied;
4. the agent kill switch blocking further work.

## Exact learning path

1. [Threat model](docs/01-threat-model.md)
2. [Build the lab](docs/02-build-lab.md)
3. [Connect PingFederate or PingOne](docs/03-ping-integration.md)
4. [Tune the security controls](docs/04-tuning-guide.md)
5. [Map Oasis and HYPR AgentPass concepts](docs/05-vendor-concept-map.md)
6. [Run incident exercises](docs/06-incident-runbook.md)
7. [Portfolio and interview guide](docs/07-portfolio-guide.md)

## Security controls demonstrated

| Control | Evidence |
|---|---|
| Unique non-human identity | `agent_id`, `owner`, token subject/client ID |
| Least privilege | scope and tool allowlists |
| Delegation boundary | action, resource, risk, time, and owner are evaluated |
| Prompt-injection defense | deterministic content signals and deny rules |
| Human-in-the-loop | high-risk actions return `REQUIRE_APPROVAL` |
| Kill switch | disabled agents are denied before tool execution |
| Accountability | structured JSON audit events with correlation IDs |
| Secure secrets | environment variables; `.env` is ignored |
| Testable policy | unit tests and CI validate expected allow/deny behavior |

## Repository layout

```text
src/agent_security/   API, identity validation, policy, guardrails, audit
config/               Agent registry and policy configuration
docs/                 No-assumptions build and tuning guides
scripts/              Safe demo and evaluation runner
tests/                Security regression tests
evidence/             Generated evaluation output (no secrets)
```

## Important limitations

- The mock mode is for learning, not production authentication.
- Production deployments must use TLS, a real Ping issuer/introspection endpoint, protected secrets, centralized logging, and an external approval channel.
- Content filters are one layer only; they do not "solve" prompt injection.
- Oasis Security and HYPR AgentPass are referenced as architectural comparisons. This repository is not affiliated with or endorsed by either vendor.

## License

MIT. See [LICENSE](LICENSE).

