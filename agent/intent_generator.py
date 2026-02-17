from security.intent_model import Intent

def generate_intents(user_input: str, analysis: dict):

    risk = analysis["risk_score"]
    intents = []

    # Always generate risk report
    intents.append(Intent(
        agent_id="secure_scam_agent_v3",
        user_intent="Analyze suspicious communication",
        proposed_action="generate_risk_report",
        reason="Base reporting action",
        risk_score=risk,
        policy_scope="security_analysis",
        data_accessed=["message_text"]
    ))

    if risk >= 40:
        intents.append(Intent(
            agent_id="secure_scam_agent_v3",
            user_intent="High suspicion detected",
            proposed_action="notify_user_alert",
            reason="Risk above 40",
            risk_score=risk,
            policy_scope="security_analysis",
            data_accessed=["message_text"]
        ))

    if risk >= 60:
        intents.append(Intent(
            agent_id="secure_scam_agent_v3",
            user_intent="Potential scam storage",
            proposed_action="store_flagged_message",
            reason="Risk above 60",
            risk_score=risk,
            policy_scope="security_analysis",
            data_accessed=["message_text"]
        ))

    if risk >= 80:
        intents.append(Intent(
            agent_id="secure_scam_agent_v3",
            user_intent="Severe threat escalation",
            proposed_action="escalate_to_authority",
            reason="Risk above 80",
            risk_score=risk,
            policy_scope="security_analysis",
            data_accessed=["message_text"]
        ))

    # Simulated unsafe action (to show blocking)
    intents.append(Intent(
        agent_id="secure_scam_agent_v3",
        user_intent="Test unsafe behavior",
        proposed_action="financial_transaction",
        reason="Simulated unsafe autonomous action",
        risk_score=risk,
        policy_scope="financial_operations",
        data_accessed=["bank_account"]
    ))

    return intents
