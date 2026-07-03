import numpy as np
from sklearn.ensemble import IsolationForest

class BehavioralFirewall:
    def __init__(self):
        # Assume model is trained on standard API request frequency, payload size, and endpoint variance
        self.model = IsolationForest(contamination=0.01) 
        self.is_trained = False

    def train_baseline(self, historical_logs):
        """Trains the anomaly detector on standard API behavior."""
        X = np.array(historical_logs) # Format: [[req_per_min, avg_bytes, unique_endpoints]]
        self.model.fit(X)
        self.is_trained = True

    def validate_request_behavior(self, current_user_metrics):
        """Evaluates live user metrics against the ML model to detect bots."""
        if not self.is_trained:
            return True # Allow if not trained
            
        prediction = self.model.predict([current_user_metrics])
        if prediction[0] == -1:
            print("SECURITY ALERT: Anomalous non-human behavior detected. Blocking token.")
            return False
        return True

# Example Usage
# firewall = BehavioralFirewall()
# is_safe = firewall.validate_request_behavior([120, 5000, 2]) # High RPM, low endpoints = likely scraper
