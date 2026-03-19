from sklearn.ensemble import IsolationForest

class AnomalyModel:

    def __init__(self):
        self.model = IsolationForest(contamination=0.3)

    def train(self, data):
        self.model.fit(data)

    def predict(self, data):
        return self.model.predict(data)