# 🌱 Disaster Alert Fatigue Control System (PS-6)

## 📌 Problem Statement  
**PS-6: Disaster Alert System with Alert Fatigue Control**

Disaster management systems often generate frequent alerts, which can overwhelm users and reduce responsiveness during real emergencies. This project focuses on **controlling alert fatigue** while ensuring that **critical disaster alerts are always delivered**.

---

## 🎯 Objective
- Reduce unnecessary alerts
- Prevent alert fatigue
- Prioritize public safety
- Provide clear, explainable alert decisions
- Allow users to control notification behavior

---

## 🧠 Solution Overview

This project implements a **rule-based, explainable decision system** that evaluates disaster alerts using:

- **Disaster Severity** (Low / Medium / High)
- **Area Risk Level** (Low / Medium / High)
- **Alert Fatigue** (derived from time since last alert)

Based on these inputs, the system decides to:
- ✅ **SEND** an alert
- ⏳ **DELAY** an alert
- 😌 **SUPPRESS** an alert

### 🚨 Critical Safety Override
If **Disaster Severity = HIGH** and **Area Risk = HIGH**,  
the alert is **always sent**, regardless of alert fatigue.

This ensures **life-critical alerts are never suppressed**.

---

## 🔍 Decision Logic Summary

| Disaster Severity | Area Risk | Alert Fatigue | Decision |
|------------------|----------|--------------|----------|
| High | High | Any | ✅ SEND |
| High | Medium | High | ⏳ DELAY |
| Medium | Medium | High | ⏳ DELAY |
| Low | Low | High | 😌 SUPPRESS |

---

## 🖥️ Key Features

- 🌿 Calm, user-friendly interface
- 🧠 Explainable alert decisions
- 🔔 Voice notifications for important alerts
- 🔕 Mute / Unmute toggle for user control
- 🚨 Safety override for high-risk disasters
- 😌 Silence for suppressed alerts to reduce stress
- 🛡️ Fail-safe handling if audio files are missing

---

## 🔊 Voice Alert Behavior

| Decision | System Response |
|--------|-----------------|
| SEND | 🔊 Voice message: “Alert sent. Please take immediate action.” |
| DELAY | 🔉 Voice message: “Alert delayed. Situation is being monitored.” |
| SUPPRESS | 🔇 No sound (intentional) |

This approach minimizes cognitive overload while maintaining situational awareness.

---

## 🧰 Technologies Used

- **Python**
- **Streamlit** (MVP & UI)
- **Rule-based Explainable AI**
- **Local Text-to-Speech (offline audio)**
- **GitHub** (version control & collaboration)

---

## 📂 Project Structure

disaster-alert-fatigue-ui-main/
├── app.py
├── alert_send.wav
├── alert_delay.wav
├── README.md


---

## ▶️ How to Run the Project

1. Install dependencies:
```bash
pip install streamlit

---

2.Navigate to the project directory:

   cd disaster-alert-fatigue-ui-main


3.Run the application:

  python -m streamlit run app.py

4.Open the local URL shown in the terminal (usually http://localhost:8501)

🧪 Example Scenario

Inputs

Disaster Severity: High

Area Risk: High

Hours Since Last Alert: 0

Output

Decision: ✅ SEND

Voice alert triggered

Explanation displayed to user

🧠 Responsible & Explainable AI Principles

Transparency through rule-based decisions

User control over alert notifications

Prevention of alert fatigue

Safety-first override for critical situations

Clear explanations for every decision

🏁 Conclusion

This system demonstrates how disaster alert mechanisms can be designed to balance safety and user well-being, ensuring critical alerts are delivered while minimizing unnecessary interruptions.

👥 Team
D.M.SHARAN
SRI HARSHA
SHAIK.HUNNURBEE

Disaster Alert Fatigue Control System
Hackathon Submission – PS-6
