import json

with open("security/policies.json") as f:
    policies = json.load(f)

def check_policy(intent):

    if intent.proposed_action in policies["blocked_actions"]:
        return False, "Blocked action type"

    if intent.policy_scope not in policies["allowed_scopes"]:
        return False, "Scope not allowed"

    if intent.risk_score > policies["max_risk_score"]:
        return False, "Risk exceeds policy threshold"

    return True, "Approved"
