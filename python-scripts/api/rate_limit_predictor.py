import datetime

class RateLimitPredictor:
    def __init__(self):
        # Peak business hours where API surges happen
        self.surge_hours = [9, 10, 11, 14, 15]

    def should_throttle_background_tasks(self):
        current_hour = datetime.datetime.now().hour
        
        if current_hour in self.surge_hours:
            print(f"[API Gateway] Peak hour ({current_hour}:00) detected. Throttling all background data syncs to prioritize live B2B traffic.")
            return True
            
        print("[API Gateway] Traffic is stable. Background tasks authorized.")
        return False

if __name__ == "__main__":
    predictor = RateLimitPredictor()
    predictor.should_throttle_background_tasks()
