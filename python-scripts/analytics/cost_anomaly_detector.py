class CostAnomalyDetector:
    def __init__(self, hourly_budget_limit=50.0):
        self.hourly_budget_limit = hourly_budget_limit

    def evaluate_spend(self, current_spend, average_spend):
        deviation = current_spend - average_spend
        
        if current_spend > self.hourly_budget_limit:
            print(f"[!] CRITICAL: Spend (${current_spend}) exceeds hard limit (${self.hourly_budget_limit}).")
            self.suspend_api_keys()
            return "suspended"
            
        if deviation > (average_spend * 2):
            print(f"[?] WARNING: Unusual token consumption spike detected. Spend is 200% above average.")
            return "warning"
            
        print("[+] Token usage within normal parameters.")
        return "safe"

    def suspend_api_keys(self):
        print("[*] Executing emergency protocol: Revoking active LLM API keys.")

if __name__ == "__main__":
    detector = CostAnomalyDetector()
    detector.evaluate_spend(current_spend=85.0, average_spend=10.0)
