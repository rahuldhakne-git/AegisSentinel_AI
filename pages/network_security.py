import streamlit as st
import time
import random

from services.graph_service import GraphService
from services.threat_service import ThreatService
from components.graph_component import draw_graph

def show():

    st.title("🌐 Network Intelligence + AI Core")

    graph_service = GraphService()
    threat_service = ThreatService()

    G = graph_service.get_graph()

    features = threat_service.detect_anomalies()

    suspicious_nodes = features[features["anomaly"] == -1]["src_ip"].values

    st.subheader("⚡ AI Threat Detection")

    if len(suspicious_nodes) > 0:
        st.error(f"🚨 Suspicious Nodes: {list(suspicious_nodes)}")
    else:
        st.success("No threats detected")

    st.subheader("🌐 Network Graph")

    graph_area = st.empty()

    attacked = []

    nodes = graph_service.get_nodes()

    # Start attack simulation
    start = random.choice(nodes)
    attacked.append(start)

    for i in range(5):

        graph_area.plotly_chart(
            draw_graph(G, suspicious_nodes, attacked),
            use_container_width=True
        )

        time.sleep(0.8)

        new_targets = []

        for node in attacked:
            new_targets += graph_service.get_neighbors(node)

        attacked = list(set(attacked + new_targets))

st.subheader("🛡️ Defense Response")

risk = random.randint(40, 95)

if risk > 80:
    st.error("🚨 Node isolated automatically")
elif risk > 60:
    st.warning("⚠️ Access restricted")
else:
    st.success("System stable")        