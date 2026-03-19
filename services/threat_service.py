import pandas as pd
from models.anomaly_model import AnomalyModel

class ThreatService:

    def __init__(self, file_path="data/network_logs.csv"):
        self.df = pd.read_csv(file_path)

    def process_data(self):
        features = self.df.groupby("src_ip").agg({
            "bytes": "sum",
            "port": "nunique"
        }).reset_index()

        return features

    def detect_anomalies(self):
        features = self.process_data()

        model = AnomalyModel()
        model.train(features[["bytes", "port"]])

        features["anomaly"] = model.predict(features[["bytes", "port"]])

        return features