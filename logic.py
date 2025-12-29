def calculate_risk(severity, area_risk):
    risk_map = {"low": 1, "medium": 2, "high": 3}
    return risk_map[severity] + risk_map[area_risk]

def calculate_fatigue(hours_since_last_alert):
    if hours_since_last_alert < 1:
        return "high"
    elif 1 <= hours_since_last_alert <= 4:
        return "medium"
    else:
        return "low"

def make_decision(risk_score, fatigue):
    if risk_score >= 5 and fatigue != "high":
        return "SEND"
    elif risk_score >= 3 and fatigue == "high":
        return "DELAY"
    else:
        return "SUPPRESS"

def explain(decision):
    if decision == "SEND":
        return "Alert sent because the disaster risk is high and alert fatigue is manageable."
    elif decision == "DELAY":
        return "Alert delayed due to existing risk but high alert fatigue."
    else:
        return "Alert suppressed to avoid unnecessary alert fatigue."
