import streamlit as st
import time
import re

class SecurityService:

    def __init__(self):
        if "login_attempts" not in st.session_state:
            st.session_state.login_attempts = 0

        if "locked" not in st.session_state:
            st.session_state.locked = False

        if "activity_log" not in st.session_state:
            st.session_state.activity_log = []

        if "last_action_time" not in st.session_state:
            st.session_state.last_action_time = time.time()

    # ---------------- LOGIN SECURITY ----------------
    def authenticate(self, username, password):

        if st.session_state.locked:
            return False, "🚨 Account locked due to multiple failed attempts"

        if username == "admin" and password == "1234":
            st.session_state.login_attempts = 0
            self.log("User logged in successfully")
            return True, "Login successful"

        st.session_state.login_attempts += 1
        self.log("Failed login attempt")

        if st.session_state.login_attempts >= 5:
            st.session_state.locked = True
            return False, "🚨 Too many attempts — system locked"

        return False, f"Invalid credentials ({st.session_state.login_attempts}/5)"

    # ---------------- INPUT VALIDATION ----------------
    def validate_input(self, text):

        dangerous_patterns = [
            r"<script>",
            r"drop",
            r"select",
            r"insert",
            r"--",
            r"union"
        ]

        for pattern in dangerous_patterns:
            if re.search(pattern, text.lower()):
                self.log(f"Blocked malicious input: {text}")
                return False

        return True

    # ---------------- RATE LIMIT ----------------
    def check_rate_limit(self):
        now = time.time()

        if now - st.session_state.last_action_time < 0.3:
            self.log("Rate limit triggered")
            return False

        st.session_state.last_action_time = now
        return True

    # ---------------- ACTIVITY LOG ----------------
    def log(self, message):
        st.session_state.activity_log.append({
            "time": time.strftime("%H:%M:%S"),
            "event": message
        })

    def get_logs(self):
        return st.session_state.activity_log[-15:]

    # ---------------- RESET SYSTEM ----------------
    def reset_security(self):
        st.session_state.login_attempts = 0
        st.session_state.locked = False
        self.log("Security system reset")