import logging
import random

class WebhookChaosInjector:
    def __init__(self, failure_probability: float = 0.05):
        self.blast_radius = failure_probability

    def intercept_and_evaluate_dry_run(self, payload_id: str) -> str:
        logging.info(f"[PORTFOLIO MOCK] Chaos Injector evaluating payload {payload_id}")
        
        chaos_roll = random.random()
        
        if chaos_roll <= self.blast_radius:
            fault_type = random.choice(["LATENCY_SPIKE", "HTTP_500", "CONNECTION_DROP"])
            logging.critical(f"[CHAOS MOCK] Fault injected: {fault_type}. Testing system resilience.")
            return fault_type
            
        logging.info("[CHAOS MOCK] Traffic passed cleanly. No fault injected.")
        return "200_OK"
