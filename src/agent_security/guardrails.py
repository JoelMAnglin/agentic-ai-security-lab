import re

def content_signals(prompt: str, policy: dict) -> list[str]:
    text = prompt.casefold()
    signals = [f"prompt_injection:{p}" for p in policy["deny_patterns"] if p.casefold() in text]
    signals += [f"sensitive_data:{p}" for p in policy["sensitive_data_patterns"] if p.casefold() in text]
    if re.search(r"https?://(?:127\.0\.0\.1|localhost|169\.254\.169\.254)", text): signals.append("ssrf_target")
    return signals

