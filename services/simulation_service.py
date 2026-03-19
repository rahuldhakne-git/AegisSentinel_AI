import random

class SimulationService:

    def __init__(self):
        self.attack_steps = [
            "Phishing Email Delivered",
            "User Credentials Compromised",
            "Unauthorized Login Detected",
            "Privilege Escalation",
            "Lateral Movement",
            "Database Access Attempt",
            "Data Exfiltration"
        ]

    def generate_attack(self):
        return self.attack_steps

    def simulate_progression(self):
        return random.sample(self.attack_steps, len(self.attack_steps))