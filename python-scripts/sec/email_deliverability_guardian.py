class DeliverabilityGuardian:
    def __init__(self, reputation_threshold=90):
        self.threshold = reputation_threshold

    def check_domain_health(self, domain, current_spam_rate):
        print(f"[SecOps] Analyzing deliverability metrics for {domain}...")
        
        if current_spam_rate > (100 - self.threshold):
            print(f"[SecOps] 🛑 ALERT: Spam rate ({current_spam_rate}%) exceeded safe limits.")
            self._pause_campaigns()
            return "Campaigns Paused"
            
        print("[SecOps] Domain reputation is healthy. Outreach proceeding as normal.")
        return "Active"

    def _pause_campaigns(self):
        print("[SecOps] Executing kill-switch on all outbound B2B cold email sequences.")

if __name__ == "__main__":
    guardian = DeliverabilityGuardian()
    guardian.check_domain_health("b2b-automations.io", current_spam_rate=12.5)
