# 7 - Portfolio and Interview Guide

## Evidence to publish safely

- Architecture diagram from the README
- Passing CI badge
- Redacted Ping configuration screenshots
- Evaluation JSON with no tokens or private URLs
- Audit event examples with fictional identities
- A short screen recording: allow, approval, injection deny, kill switch

## Suggested résumé bullets

Use only after you have personally run and validated the lab:

- Built a Ping-compatible agentic AI security gateway enforcing OAuth scopes, agent-to-owner identity binding, tool allowlists, risk-based human approval, and kill-switch controls for non-human identities.
- Developed automated security regression tests covering prompt injection, missing scopes, confused-deputy behavior, unapproved tools, and disabled-agent enforcement.
- Mapped vendor-neutral controls to Oasis non-human identity governance and HYPR AgentPass identity, enforcement, and accountability patterns; documented incident response and policy-tuning procedures.

## Demo script

1. Explain why agents require stronger controls than chatbots.
2. Show `agents.yaml` and ownership/least privilege.
3. Run the safe action and show `ALLOW`.
4. Run a risky action and show `REQUIRE_APPROVAL`.
5. Run prompt injection and show `DENY`.
6. Disable the agent and show the kill switch.
7. Open the audit event and trace the correlation ID.
8. Explain how Ping JWT/introspection replaces mock authentication.

## Questions you should be able to answer

- Why is model-level filtering insufficient?
- How do you prevent a confused-deputy attack?
- Why use short-lived workload identity instead of a shared API key?
- What actions require human approval?
- How do you measure false allows and false denies?
- How do you revoke an agent in an incident?
- How do Oasis and HYPR AgentPass differ from traditional workforce IAM?

