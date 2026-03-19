import streamlit as st
from services.security_service import SecurityService

def show():
    sec = SecurityService()

    st.title("🛡️ Security Center")

    col1, col2 = st.columns(2)

    col1.metric("Login Attempts", st.session_state.get("login_attempts", 0))
    col2.metric("System Lock Status", "LOCKED" if st.session_state.get("locked") else "ACTIVE")

    st.subheader("📜 Activity Logs")

    logs = sec.get_logs()

    if logs:
        for log in logs:
            st.write(f"{log['time']} → {log['event']}")
    else:
        st.info("No activity yet")

    st.subheader("⚙️ Controls")

    if st.button("Reset Security System"):
        sec.reset_security()
        st.success("System reset complete")