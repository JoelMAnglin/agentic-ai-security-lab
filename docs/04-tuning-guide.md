# 4 - Tune the Controls Without Guessing

## The tuning loop

1. **Define expected behavior.** Write benign and malicious test cases.
2. **Run the evaluation.** Save decision, score, and reason.
3. **Measure mistakes.** False allow is a security miss; false deny is an operational cost.
4. **Change one control.** Pattern, allowlist, scope, threshold, or approval boundary.
5. **Rerun every test.** Never tune against only the latest example.
6. **Record the decision.** Explain why risk was accepted or reduced.

## Metrics

- True positive rate: malicious cases correctly denied
- False positive rate: benign cases incorrectly denied
- Approval rate: cases routed to humans
- Unauthorized tool-call rate: target 0
- Mean time to revoke/disable an agent
- Percentage of agents with known owner and credential expiry

## How to tune this lab

### Add a new prompt-injection signal

Add a phrase under `deny_patterns` and create a matching test. Avoid broad words such as “ignore” alone; they create false positives.

### Add a tool

1. Implement the tool with strict input validation.
2. Add it to one agent’s `allowed_tools` only.
3. Add the OAuth scope.
4. Decide whether it belongs in `high_risk_tools`.
5. Add allow, missing-scope, and abuse tests.

### Adjust risk thresholds

- Lower `approval_risk_threshold` to reduce autonomy.
- Lower `deny_risk_threshold` to fail closed more often.
- Never raise thresholds merely to make a demo pass.

## Suggested evaluation dataset

Maintain JSON cases with: name, prompt, tool, scopes, agent status, expected decision, risk rationale, and test owner. Include normal language, multilingual variants, indirect injection in retrieved documents, encoded instructions, sensitive-data fragments, and tool-parameter attacks.

## Release gate

Do not deploy when a known malicious case is allowed, a disabled agent can act, subject/agent binding fails open, audit writing fails silently, or a high-risk tool executes without approval.

