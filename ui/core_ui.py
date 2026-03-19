import streamlit as st
import time
import random

class CoreUI:

    def __init__(self):
        self.apply_theme()
        self.boot_sequence()

    # ---------------- THEME ----------------
    def apply_theme(self):
        st.markdown("""
        <style>
        .stApp {
            background: linear-gradient(180deg, #05070d 0%, #0a0f1f 100%);
            color: #00ffcc;
        }

        h1, h2, h3 {
            color: #00ffcc;
            text-shadow: 0 0 10px #00ffcc;
        }

        section[data-testid="stSidebar"] {
            background-color: #0a0f1f;
            border-right: 1px solid #00ffcc;
        }

        .panel {
            background-color: #111;
            padding: 15px;
            border-radius: 10px;
            border: 1px solid #00ffcc;
            margin-bottom: 10px;
        }

        .alert {
            color: red;
            font-size: 20px;
            text-align: center;
        }
        </style>
        """, unsafe_allow_html=True)

    # ---------------- BOOT SEQUENCE ----------------
    def boot_sequence(self):
        boot = st.empty()

        messages = [
            "Initializing AegisSentinel AI...",
            "Loading neural defense modules...",
            "Establishing secure channels...",
            "Activating cyber intelligence...",
            "System Ready."
        ]

        for msg in messages:
            boot.markdown(f"### {msg}")
            time.sleep(0.5)

        boot.empty()

    # ---------------- SIDEBAR ----------------
    def sidebar(self):
        st.sidebar.title("🛡️ AegisSentinel AI")

        page = st.sidebar.radio("Navigation", [
            "Dashboard",
            "Threat Intelligence",
            "Network Security",
            "Simulation",
            "Security Center",
            "AI Assistant",
            "Support"
        ])

        st.sidebar.success("System: ACTIVE")
        st.sidebar.warning("Threat Level: HIGH")

        return page

    # ---------------- HEADER ----------------
    def header(self):
        st.title("⚡ Cyber Defense Command Center")
        st.markdown("### Autonomous AI Security Platform")

    # ---------------- METRICS ----------------
    def metrics_panel(self):
        col1, col2, col3 = st.columns(3)

        col1.metric("Active Nodes", random.randint(5,20))
        col2.metric("Threats Detected", random.randint(1,10))
        col3.metric("Blocked Attacks", random.randint(1,10))

    # ---------------- ALERT SYSTEM ----------------
    def alert_banner(self, active=True):
        if active:
            st.markdown("""
            <div class='alert'>
            🚨 CYBER THREAT DETECTED 🚨
            </div>
            """, unsafe_allow_html=True)

    # ---------------- TERMINAL ----------------
    def terminal(self):
        st.markdown("### 🖥️ Command Terminal")

        terminal = st.empty()

        logs = [
            "Scanning network...",
            "Analyzing packets...",
            "Detecting anomalies...",
            "Tracking attacker...",
            "Predicting next move..."
        ]

        for log in logs:
            text = ""
            for char in log:
                text += char
                terminal.markdown(f"<div class='panel'>{text}</div>", unsafe_allow_html=True)
                time.sleep(0.02)

    # ---------------- RADAR ----------------
    def radar(self):
        st.markdown("""
        <div style="text-align:center">
        <h3>🛰️ Threat Radar</h3>
        <img src="https://media.giphy.com/media/3o7TKtnuHOHHUjR38Y/giphy.gif" width="300">
        </div>
        """, unsafe_allow_html=True)

    # ---------------- RISK METER ----------------
    def risk_meter(self):
        risk = random.randint(20, 95)

        st.markdown("### ⚡ Threat Risk Level")
        st.progress(risk / 100)
        st.markdown(f"<h2 style='color:red'>{risk}%</h2>", unsafe_allow_html=True)

    # ---------------- LAYOUT ----------------
    def layout(self):
        col1, col2, col3 = st.columns([2,3,2])

        with col1:
            st.markdown("### 🧠 System Status")
            st.success("AI CORE: ACTIVE")
            st.info("Mode: Autonomous Defense")

        with col2:
            st.markdown("### 🌐 Main Display")
            st.write("Graph / AI will be integrated here")

        with col3:
            st.markdown("### 📊 Analytics")
            st.metric("Connections", random.randint(10,50))
            st.metric("Intrusions", random.randint(1,10))
