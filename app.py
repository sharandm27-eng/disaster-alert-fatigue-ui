import streamlit as st
from logic import calculate_risk, calculate_fatigue, make_decision, explain

st.title("Disaster Alert System – UI Prototype")

severity = st.selectbox("Disaster Severity", ["low", "medium", "high"])
area_risk = st.selectbox("Area Risk Level", ["low", "medium", "high"])
hours = st.slider("Hours since last alert", 0, 24, 2)

if st.button("Check Alert Decision"):
    risk_score = calculate_risk(severity, area_risk)
    fatigue = calculate_fatigue(hours)
    decision = make_decision(risk_score, fatigue)
    explanation = explain(decision)

    st.subheader("Decision Result")
    st.write(f"**Decision:** {decision}")
    st.write(f"**Explanation:** {explanation}")
