from .guardrails import content_signals
from .models import ActionRequest, Decision, PolicyResult, Principal

def required_scope(tool: str) -> str:
    return tool.replace(".", ":")

def evaluate(principal: Principal, req: ActionRequest, registry: dict, policy: dict) -> PolicyResult:
    reasons=[]; risk=0; agent=registry.get("agents", {}).get(req.agent_id)
    scope=required_scope(req.tool)
    if not agent: return PolicyResult(decision=Decision.DENY,risk_score=100,reasons=["unknown_agent"],required_scope=scope)
    if not agent.get("enabled"): return PolicyResult(decision=Decision.DENY,risk_score=100,reasons=["kill_switch_active"],required_scope=scope)
    if principal.subject != req.agent_id: reasons.append("subject_agent_mismatch"); risk += 80
    if "agent:run" not in principal.scopes or scope not in principal.scopes: reasons.append("missing_scope"); risk += 80
    if req.tool not in agent.get("allowed_tools", []): reasons.append("tool_not_allowlisted"); risk += 60
    signals=content_signals(req.prompt,policy)
    if signals: reasons.extend(signals); risk += 80
    if req.tool in policy.get("high_risk_tools",[]): reasons.append("high_risk_tool"); risk += 50
    risk=min(risk,100)
    if risk >= policy["deny_risk_threshold"]: decision=Decision.DENY
    elif risk >= policy["approval_risk_threshold"] or risk > agent["max_risk_without_approval"]: decision=Decision.REQUIRE_APPROVAL
    else: decision=Decision.ALLOW
    if not reasons: reasons=["policy_checks_passed"]
    return PolicyResult(decision=decision,risk_score=risk,reasons=reasons,required_scope=scope)

