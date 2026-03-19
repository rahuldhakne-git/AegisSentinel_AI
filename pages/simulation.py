import streamlit as st
import time
import random

from services.simulation_service import SimulationService
from services.defense_service import DefenseService

def show():

    st.title("🔥 AI Attack Simulation + Defense System")

    sim = SimulationService()
    defense = DefenseService()

    st.subheader("⚡ Attack Scenario")

    steps = sim.generate_attack()

    progress_bar = st.progress(0)

    anomaly_score = random.randint(30, 90)

    spread_factor = 0

    for i, step in enumerate(steps):

        st.error(f"⚠️ {step}")

        spread_factor += random.randint(5, 15)

        progress_bar.progress((i + 1) / len(steps))

        time.sleep(0.8)

    st.subheader("📊 Risk Analysis")

    risk = defense.calculate_risk(anomaly_score, spread_factor)

    st.metric("Threat Risk Score", f"{risk}%")

    st.progress(risk / 100)

    st.subheader("🛡️ AI Defense Decision")

    action = defense.decide_action(risk)

    st.success(action)