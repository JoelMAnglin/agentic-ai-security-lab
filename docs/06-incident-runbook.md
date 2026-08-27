# 6 - Agent Security Incident Runbook

## Trigger examples

- Agent attempts a forbidden tool
- Prompt injection is detected
- Token is used by the wrong agent
- Large increase in approval requests
- Unknown agent or ownerless credential appears
- Audit chain or telemetry becomes unavailable

## Containment

1. Set the agent’s `enabled` value to `false`.
2. Revoke the Ping client/token and rotate credentials.
3. Disable tool/API access independently of the model.
4. Preserve prompts, tool calls, approval records, tokens’ metadata (not raw secrets), and audit events.
5. Identify the human owner and affected resources.

## Investigation

- Trace `correlation_id` from human request through agent, policy, tool, and result.
- Compare requested scope with granted scope.
- Determine whether untrusted content influenced planning.
- Check memory/RAG writes and downstream agent messages.
- Identify every credential and resource touched.

## Recovery

- Correct the policy or integration.
- Add a regression test reproducing the incident.
- Rotate credentials and shorten lifetime if appropriate.
- Re-enable in a restricted canary mode.
- Monitor for recurrence.

## Post-incident questions

- Why was the agent able to request the action?
- Why did preventive controls not stop it earlier?
- Was human approval meaningful and attributable?
- Could the same identity reach other systems?
- Did logs contain enough context without exposing secrets?

