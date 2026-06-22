import time

class PredictiveAutoScaler:
    def __init__(self, limit_per_minute):
        self.limit = limit_per_minute
        self.current_usage = 0

    def route_request(self):
        usage_percentage = (self.current_usage / self.limit) * 100
        
        if usage_percentage >= 90:
            print(f"[API Gateway] ⚠️ Traffic at {usage_percentage}%. Activating dynamic throttling to prevent 429 Ban.")
            time.sleep(2) # Enforce artificial delay
            self.current_usage += 1
            return "Request Processed (Throttled)"
            
        self.current_usage += 1
        return "Request Processed (Normal Speed)"

if __name__ == "__main__":
    scaler = PredictiveAutoScaler(limit_per_minute=100)
    scaler.current_usage = 91 # Simulating high load
    print(scaler.route_request())
