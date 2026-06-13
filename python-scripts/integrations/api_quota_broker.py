import logging

class MultiTenantQuotaBroker:
    def __init__(self, api_key_pool: dict):
        self.key_pool = api_key_pool

    def get_optimal_key_dry_run(self) -> str:
        logging.info("[PORTFOLIO MOCK] Brokering optimal API key for outbound request...")
        
        for key_name, metrics in self.key_pool.items():
            usage_percentage = (metrics["used"] / metrics["limit"]) * 100
            
            if usage_percentage < 95.0:
                logging.info(f"[INTEGRATION MOCK] Traffic routed via {key_name} (Usage: {usage_percentage:.1f}%).")
                return metrics["token"]
                
            logging.warning(f"[INTEGRATION MOCK] Key {key_name} exhausted. Shifting to fallback.")
            
        logging.critical("[FATAL] All integration API keys have exhausted their quotas.")
        return "ERROR_QUOTA_EXCEEDED"
