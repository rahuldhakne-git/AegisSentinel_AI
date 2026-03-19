import streamlit as st
import time

def show_entry():

    container = st.empty()

    messages = [
        "Initializing AegisSentinel AI...",
        "Loading Cyber Defense Modules...",
        "Connecting to Secure Network...",
        "Activating AI Intelligence...",
        "Scanning Environment...",
        "System Online"
    ]

    for msg in messages:
        container.markdown(f"### {msg}")
        time.sleep(0.6)

    container.empty()