# 2 - Build the Lab Step by Step

## Step 1: Verify Python

```bash
python --version
```

Use Python 3.11 or newer.

## Step 2: Create and activate the environment

Follow the OS-specific commands in the README, then install requirements.

## Step 3: Understand the configuration

Open `config/agents.yaml`. Each agent has:

- `owner`: accountable human or team
- `enabled`: kill switch
- `allowed_tools`: exact tool names
- `allowed_scopes`: OAuth permissions
- `max_risk_without_approval`: autonomy ceiling

Open `config/policy.yaml`. It contains content signals and decision thresholds. Configuration is not code, which makes reviews and tuning easier.

## Step 4: Run tests before starting the service

```bash
pytest -q
```

Expected: all tests pass. A failed security test is a release blocker.

## Step 5: Start the gateway

```bash
uvicorn agent_security.api:app --app-dir src --reload
```

The gateway validates the identity, evaluates policy, writes an audit event, and only then calls a safe tool implementation.

## Step 6: Run the demo

```bash
python scripts/demo.py
```

Mock tokens are deliberately insecure and exist only so a beginner can see the full decision path without a Ping tenant.

## Step 7: Generate tuning evidence

```bash
set PYTHONPATH=src
python scripts/evaluate_policy.py
```

On macOS/Linux use `export PYTHONPATH=src`. Review `evidence/policy-evaluation.json`.

## Step 8: Inspect the audit log

Each line is JSON and includes the timestamp, correlation ID, owner, agent, subject, tool, decision, risk, reasons, and a SHA-256 event hash. In production, send these events to a SIEM with append-only retention.

