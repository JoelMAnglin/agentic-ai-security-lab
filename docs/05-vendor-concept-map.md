# 5 - Oasis and HYPR AgentPass Concept Map

This is a learning comparison based on public vendor descriptions, not a product implementation or endorsement.

| Industry concept | Lab implementation | Oasis-style emphasis | HYPR AgentPass-style emphasis |
|---|---|---|---|
| Agent inventory | `config/agents.yaml` | Discover agents/NHIs and ownership | Know and govern active agents |
| Verifiable identity | Token subject = agent ID | Identity-based control | Identity bound to human owner |
| Least privilege | Scopes and tool allowlists | Entitlement cleanup and lifecycle | Defined scope of authority |
| Time-bounded delegation | Token lifetime (Ping) | JIT identity and rotation | Time-bounded agent session |
| Inline enforcement | `policy.evaluate()` before tools | Policy at action boundary | Enforce at source/endpoint |
| Human supervision | `REQUIRE_APPROVAL` | Approval for sensitive intent | Approve, deny, constrain, terminate |
| Kill switch | `enabled: false` | Deprovision/revoke NHI | Terminate agent immediately |
| Accountability | Correlated audit event | Agent/identity/permission visibility | Human-agent-action chain |

## Interview explanation

“I built a vendor-neutral control plane for agentic identities. Ping-compatible OAuth establishes the workload identity; a policy enforcement point binds the token subject to a registered agent, checks scopes and tool entitlements, detects unsafe content, and returns allow, deny, or human approval. The design maps to Oasis non-human identity governance and HYPR AgentPass identity, enforcement, and accountability patterns.”

