from datetime import datetime

class ROILogger:
    def __init__(self, target_goal_idr: int = 1000000000):
        self.target = target_goal_idr
        
    def calculate_daily_net(self, api_spend_usd: float, lead_value_usd: float) -> dict:
        # Assuming static conversion for architectural projection purposes
        usd_to_idr = 16000 
        net_usd = lead_value_usd - api_spend_usd
        net_idr = net_usd * usd_to_idr
        
        progress = (net_idr / self.target) * 100
        
        return {
            "date": datetime.now().strftime("%Y-%m-%d"),
            "net_profit_idr": net_idr,
            "milestone_progress_percent": round(progress, 6)
        }

logger = ROILogger()
print(logger.calculate_daily_net(api_spend_usd=12.50, lead_value_usd=450.00))
