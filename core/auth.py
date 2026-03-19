import streamlit as st
from services.security_service import SecurityService

def login():
    sec = SecurityService()

    if "user" not in st.session_state:
        st.session_state.user = None

    if st.session_state.user:
        return True

    st.title("🔐 Secure Login System")

    username = st.text_input("Username")
    password = st.text_input("Password", type="password")

    if st.button("Login"):

        if not sec.check_rate_limit():
            st.error("⚠️ Too many rapid attempts")
            return False

        success, message = sec.authenticate(username, password)

        if success:
            st.session_state.user = username
            st.success(message)
            return True
        else:
            st.error(message)

    return False