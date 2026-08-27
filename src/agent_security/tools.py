SAFE_DATA={"INC-1001":{"status":"open","severity":"medium"}}

def execute(tool: str, resource: str, action: str) -> dict:
    if tool == "ticket.read": return SAFE_DATA.get(resource,{"status":"not_found"})
    if tool == "ticket.comment": return {"status":"comment_recorded","ticket":resource,"comment":action[:120]}
    if tool == "intel.lookup": return {"indicator":resource,"verdict":"unknown","source":"safe-demo"}
    raise ValueError("tool has no safe implementation")

