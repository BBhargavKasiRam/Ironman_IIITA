from pydantic import BaseModel
from typing import List

class Intent(BaseModel):
    agent_id: str
    user_intent: str
    proposed_action: str
    reason: str
    risk_score: int
    policy_scope: str
    data_accessed: List[str]
