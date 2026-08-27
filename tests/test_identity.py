import base64,json,pytest
from agent_security.identity import validate_mock_token

def test_mock_token():
    t=base64.urlsafe_b64encode(json.dumps({"sub":"soc-helper","scope":"agent:run ticket:read"}).encode()).decode().rstrip("=")
    p=validate_mock_token(t); assert p.subject=="soc-helper" and "ticket:read" in p.scopes
def test_bad_mock_token():
    with pytest.raises(ValueError): validate_mock_token("bad")

