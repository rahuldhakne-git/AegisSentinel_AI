class DefenseService:

    def calculate_risk(self, anomaly_score, spread_factor):

        risk = (anomaly_score * 0.6) + (spread_factor * 0.4)

        return min(100, int(risk))

    def decide_action(self, risk):

        if risk > 80:
            return "🚨 CRITICAL: Isolate Node + Block IP"
        elif risk > 60:
            return "⚠️ HIGH: Restrict Access + Monitor"
        elif risk > 40:
            return "🟡 MEDIUM: Alert Admin"
        else:
            return "🟢 LOW: Safe"