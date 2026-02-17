from security.policy_engine import check_policy
from security.audit_logger import log_event

def enforce_intent(intent):

    allowed, reason = check_policy(intent)

    if allowed:
        log_event(intent, "APPROVED")
        return {"status": "approved"}
    else:
        log_event(intent, "BLOCKED")
        return {
            "status": "blocked",
            "reason": reason
        }
