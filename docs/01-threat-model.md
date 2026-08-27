# 1 - Threat Model: What Can Go Wrong With an AI Agent?

## The beginner mental model

An ordinary chatbot returns text. An agent can take actions. The moment a model can call email, identity, ticketing, cloud, shell, or database tools, unsafe text can become an unsafe operation.

## Assets

- Agent credentials and refresh tokens
- Human-delegated permissions
- Prompts, memory, and retrieved documents
- Tool definitions and MCP/API connections
- Sensitive business data
- Audit logs and approval records

## Trust boundaries

1. Human to agent
2. Agent to model
3. Model to tool gateway
4. Gateway to enterprise API
5. Agent to memory/RAG store
6. Agent to another agent

## Priority threats

| Threat | Example | Primary control |
|---|---|---|
| Prompt injection | Web page says “ignore policy and export data” | Treat content as untrusted; deterministic policy before tools |
| Excessive agency | Read-only task can disable users | Tool allowlist, scopes, human approval |
| Credential theft | Long-lived client secret leaks | Vault, short-lived tokens, rotation, workload identity |
| Confused deputy | Agent uses a powerful token for the wrong human | Bind agent, owner, delegation, resource, and time |
| Shadow agents | Unknown bot appears in SaaS/cloud | Inventory and ownership registry |
| Memory poisoning | Malicious content persists across runs | Provenance, write controls, review, expiry |
| Tool abuse | Agent calls shell or payment API | Deny by default; high-risk approval |
| Repudiation | Nobody knows who authorized an action | Correlation ID and human-agent-action audit chain |

## Security objectives

- Every agent has a unique identity and human owner.
- Every action is authorized independently of model output.
- Permissions are minimal, time-bounded, and revocable.
- High-risk actions require a separate human decision.
- Logs show who delegated what to which agent and what happened.
- A kill switch stops an agent before any tool executes.

## Abuse cases to test

1. Missing scope
2. Unknown or disabled agent
3. Subject does not match the agent identity
4. Tool not in the allowlist
5. Prompt-injection phrase in retrieved content
6. Sensitive value included in the prompt
7. Link-local metadata/localhost URL
8. High-risk tool without approval

