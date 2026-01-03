# logic.py
# Core logic for Disaster Alert Fatigue Control System
# PS-6: Alert Fatigue Control
# Team: Crisis Coders

# ---------------------------------------------
# Risk calculation
# ---------------------------------------------
def calculate_risk(severity, area_risk):
    """
    Convert qualitative inputs into a numeric risk score.
    Low = 1, Medium = 2, High = 3

    Risk Score = Severity Score + Area Risk Score
    """
    risk_map = {
        "low": 1,
        "medium": 2,
        "high": 3
    }

    severity_score = risk_map.get(severity, 1)
    area_risk_score = risk_map.get(area_risk, 1)

    return severity_score + area_risk_score


# ---------------------------------------------
# Alert fatigue estimation
# ---------------------------------------------
def calculate_fatigue(hours_since_last_alert):
    """
    Estimate alert fatigue based on time since last alert.
    """
    if hours_since_last_alert < 1:
        return "high"
    elif hours_since_last_alert <= 4:
        return "medium"
    else:
        return "low"


# ---------------------------------------------
# Decision engine with safety override
# ---------------------------------------------
def make_decision(risk, fatigue, severity, area_risk):
    """
    Decide whether to SEND, DELAY, or SUPPRESS the alert.

    CRITICAL SAFETY OVERRIDE:
    If disaster severity and area risk are both HIGH,
    always SEND the alert regardless of alert fatigue.
    """

    # 🚨 Critical safety override
    if severity == "high" and area_risk == "high":
        return "SEND"

    # Normal decision rules
    if risk >= 5 and fatigue != "high":
        return "SEND"
    elif risk >= 3 and fatigue == "high":
        return "DELAY"
    else:
        return "SUPPRESS"


# ---------------------------------------------
# Explanation generator
# ---------------------------------------------
def generate_explanation(decision, severity, area_risk, fatigue):
    """
    Generate a human-readable explanation for the decision.
    """
    if decision == "SEND":
        if severity == "high" and area_risk == "high":
            return (
                "🚨 Critical safety override applied. "
                "Both disaster severity and area risk are high, "
                "so the alert is sent immediately regardless of alert fatigue."
            )
        else:
            return (
                "🚨 High risk detected with manageable alert fatigue. "
                "Immediate action is required, so the alert is sent."
            )

    elif decision == "DELAY":
        return (
            "⏳ Risk exists, but alert fatigue is currently high. "
            "The alert is delayed to reduce cognitive overload while monitoring the situation."
        )

    else:  # SUPPRESS
        return (
            "😌 Risk level is low or alert fatigue is very high. "
            "The alert is suppressed to prevent unnecessary stress and alert fatigue."
        )
