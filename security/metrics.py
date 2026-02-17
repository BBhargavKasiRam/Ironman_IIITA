metrics = {
    "total_requests": 0,
    "total_actions": 0,
    "approved_actions": 0,
    "blocked_actions": 0,
    "high_risk_messages": 0
}

def update_metrics(analysis, action_results):
    metrics["total_requests"] += 1
    metrics["total_actions"] += len(action_results)

    if analysis["risk_score"] >= 80:
        metrics["high_risk_messages"] += 1

    for result in action_results:
        if result["execution_result"].get("status") == "blocked":
            metrics["blocked_actions"] += 1
        else:
            metrics["approved_actions"] += 1

def get_metrics():
    return metrics
