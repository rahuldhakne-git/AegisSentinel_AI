import streamlit as st

st.title("AegisSentinel AI")
st.write("System Initialized")

#-----------CORE BODY ui/core_ui.py  --------

from ui.core_ui import CoreUI

ui = CoreUI()

ui.header()
page = ui.sidebar()

ui.metrics_panel()
ui.alert_banner()
ui.layout()
ui.terminal()
ui.radar()
ui.risk_meter()

#-----------ui entry animation ui/entry_animation.py --------
from ui.entry_animation import show_entry

show_entry()


