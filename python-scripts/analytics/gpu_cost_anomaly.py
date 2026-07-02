import numpy as np

def detect_cost_anomaly(historical_daily_costs, current_cost):
    """Detects if today's serverless AI cost exceeds standard deviation thresholds."""
    if len(historical_daily_costs) < 7:
        return False # Need baseline data
        
    mean_cost = np.mean(historical_daily_costs)
    std_dev = np.std(historical_daily_costs)
    
    # Alert if current cost is more than 3 standard deviations above the mean
    anomaly_threshold = mean_cost + (3 * std_dev)
    
    if current_cost > anomaly_threshold:
        print(f"FINOPS ALERT: Anomaly detected! Current cost ${current_cost} exceeds threshold ${anomaly_threshold:.2f}")
        # Webhook trigger to PagerDuty would execute here
        return True
        
    print(f"FinOps check passed. Current cost ${current_cost} is within normal variance.")
    return False

if __name__ == "__main__":
    detect_cost_anomaly([120, 135, 125, 140, 130, 122, 138], 450) # Will trigger alert
