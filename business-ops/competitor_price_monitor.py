import hashlib

class PricingMonitor:
    def __init__(self):
        # Baseline hashes of competitor pricing pages
        self.baselines = {"comp_a": "a1b2c3d4", "comp_b": "e5f6g7h8"}

    def check_for_changes(self, competitor_id, current_html):
        current_hash = hashlib.md5(current_html.encode()).hexdigest()
        
        if current_hash != self.baselines.get(competitor_id):
            print(f"[-] ALERT: Pricing change detected for {competitor_id}!")
            self._trigger_sales_alert(competitor_id)
            self.baselines[competitor_id] = current_hash
            return True
        return False

    def _trigger_sales_alert(self, competitor_id):
        print(f"[*] Dispatching webhook alert to Sales Slack channel regarding {competitor_id}.")

if __name__ == "__main__":
    monitor = PricingMonitor()
    # Simulating a changed HTML structure from a competitor
    monitor.check_for_changes("comp_a", "<html>$19/month changed to $15/month</html>")
