import streamlit as st
import os

# --------------------------------------------------
# Page Configuration
# --------------------------------------------------
st.set_page_config(
    page_title="Disaster Alert Fatigue Control",
    page_icon="🌱",
    layout="centered"
)

# --------------------------------------------------
# Session State for Sound Toggle
# --------------------------------------------------
if "sound_on" not in st.session_state:
    st.session_state.sound_on = True

# --------------------------------------------------
# Custom CSS (Peaceful Green Theme)
# --------------------------------------------------
st.markdown("""
<style>
    .stApp {
        background: linear-gradient(to bottom right, #e8f5e9, #f1f8e9);
    }
    .main-title {
        text-align: center;
        font-size: 36px;
        font-weight: 700;
        color: #1b5e20;
    }
    .subtitle {
        text-align: center;
        font-size: 16px;
        color: #4caf50;
        margin-bottom: 25px;
    }
    .card {
        background-color: white;
        padding: 25px;
        border-radius: 15px;
        box-shadow: 0px 8px 20px rgba(0,0,0,0.08);
        margin-bottom: 20px;
    }
</style>
""", unsafe_allow_html=True)

# --------------------------------------------------
# Decision Logic (MVP)
# --------------------------------------------------
def calculate_risk(severity, area_risk):
    risk_map = {"low": 1, "medium": 2, "high": 3}
    return risk_map[severity] + risk_map[area_risk]

def calculate_fatigue(hours):
    if hours < 1:
        return "high"
    elif hours <= 4:
        return "medium"
    else:
        return "low"

def make_decision(risk, fatigue, severity, area_risk):
    # 🚨 CRITICAL OVERRIDE RULE
    # If both disaster severity and area risk are HIGH,
    # always SEND the alert regardless of alert fatigue
    if severity == "high" and area_risk == "high":
        return "SEND"

    # Normal rules
    if risk >= 5 and fatigue != "high":
        return "SEND"
    elif risk >= 3 and fatigue == "high":
        return "DELAY"
    else:
        return "SUPPRESS"


def explain(decision):
    explanations = {
        "SEND": "🚨 Immediate action required. High risk detected with manageable alert fatigue.",
        "DELAY": "⏳ Risk exists, but frequent alerts may overwhelm users. Alert delayed for confirmation.",
        "SUPPRESS": "😌 Low risk or excessive alert fatigue. Alert suppressed to maintain public calm."
    }
    return explanations[decision]

# --------------------------------------------------
# Header
# --------------------------------------------------
st.markdown("<div class='main-title'>🌱 Disaster Alert Fatigue Control</div>", unsafe_allow_html=True)
st.markdown(
    "<div class='subtitle'>Explainable & Responsible AI for disaster alert decisions</div>",
    unsafe_allow_html=True
)

# --------------------------------------------------
# Sound Toggle
# --------------------------------------------------
st.toggle(
    "🔔 Voice Notification",
    value=st.session_state.sound_on,
    key="sound_on"
)

# --------------------------------------------------
# Input Card
# --------------------------------------------------
st.markdown("<div class='card'>", unsafe_allow_html=True)
st.subheader("📥 Alert Input Parameters")

col1, col2 = st.columns(2)

with col1:
    severity = st.selectbox(
        "🔥 Disaster Severity",
        ["low", "medium", "high"]
    )

with col2:
    area_risk = st.selectbox(
        "📍 Area Risk Level",
        ["low", "medium", "high"]
    )

hours = st.slider(
    "⏱ Hours Since Last Alert",
    min_value=0,
    max_value=10,
    value=2
)

st.markdown("</div>", unsafe_allow_html=True)

# --------------------------------------------------
# Decision Button & Output
# --------------------------------------------------
if st.button("🧠 Evaluate Alert Decision", use_container_width=True):
    risk = calculate_risk(severity, area_risk)
    fatigue = calculate_fatigue(hours)
    decision = make_decision(risk, fatigue, severity, area_risk)
    explanation = explain(decision)

    # 🔊 SAFE voice playback (checks file existence)
    if st.session_state.sound_on:
        base_path = os.path.dirname(__file__)

        if decision == "SEND":
            send_audio = os.path.join(base_path, "alert_send.wav")
            if os.path.exists(send_audio):
                st.audio(send_audio, format="audio/wav", autoplay=True)

        elif decision == "DELAY":
            delay_audio = os.path.join(base_path, "alert_delay.wav")
            if os.path.exists(delay_audio):
                st.audio(delay_audio, format="audio/wav", autoplay=True)
        # SUPPRESS → no sound (intentional)

    st.markdown("<div class='card'>", unsafe_allow_html=True)
    st.subheader("📊 Decision & Explanation")

    if decision == "SEND":
        st.success(f"✅ **Decision: {decision}**")
    elif decision == "DELAY":
        st.warning(f"⚠️ **Decision: {decision}**")
    else:
        st.info(f"ℹ️ **Decision: {decision}**")

    st.markdown(explanation)
    st.markdown("</div>", unsafe_allow_html=True)

# --------------------------------------------------
# Footer
# --------------------------------------------------
st.markdown(
    "<center style='color:#2e7d32;'>🧠 Responsible & Explainable AI | PS-6: Alert Fatigue Control</center>",
    unsafe_allow_html=True
)
