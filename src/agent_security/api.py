from fastapi import FastAPI, Header, HTTPException
from .audit import write_event
from .config import load_yaml, settings
from .identity import validate_token
from .models import ActionRequest, Decision
from .policy import evaluate
from .tools import execute

app=FastAPI(title="Agentic AI Security Gateway",version="1.0.0")

@app.get("/health")
def health(): return {"status":"ok"}

@app.post("/v1/actions")
def action(req: ActionRequest, authorization: str = Header(...)):
    if not authorization.startswith("Bearer "): raise HTTPException(401,"Bearer token required")
    cfg=settings()
    try: principal=validate_token(authorization.removeprefix("Bearer "),cfg)
    except Exception as exc: raise HTTPException(401,"invalid token") from exc
    result=evaluate(principal,req,load_yaml("agents.yaml"),load_yaml("policy.yaml"))
    event={"correlation_id":req.correlation_id,"agent_id":req.agent_id,"owner":load_yaml("agents.yaml").get("agents",{}).get(req.agent_id,{}).get("owner"),"subject":principal.subject,"tool":req.tool,"resource":req.resource,"decision":result.decision,"risk_score":result.risk_score,"reasons":result.reasons}
    write_event(cfg["audit_log_path"],event)
    if result.decision == Decision.DENY: raise HTTPException(403,result.model_dump())
    if result.decision == Decision.REQUIRE_APPROVAL: return {"result":result,"approval_id":f"approve-{req.correlation_id}"}
    return {"result":result,"tool_output":execute(req.tool,req.resource,req.action)}

