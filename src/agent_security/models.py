from enum import StrEnum
from pydantic import BaseModel, Field

class Decision(StrEnum):
    ALLOW = "ALLOW"
    DENY = "DENY"
    REQUIRE_APPROVAL = "REQUIRE_APPROVAL"

class Principal(BaseModel):
    subject: str
    scopes: set[str] = Field(default_factory=set)
    issuer: str = "mock://local"

class ActionRequest(BaseModel):
    agent_id: str
    tool: str
    action: str
    resource: str
    prompt: str = ""
    correlation_id: str

class PolicyResult(BaseModel):
    decision: Decision
    risk_score: int = Field(ge=0, le=100)
    reasons: list[str]
    required_scope: str

