import logging

class WebhookCircuitBreaker:
    def __init__(self, failure_threshold: int = 3):
        self.threshold = failure_threshold
        self.consecutive_failures = 0
        self.state = "CLOSED" # CLOSED means traffic flows normally

    def handle_request_dry_run(self, payload: dict, downstream_status: int):
        logging.info(f"[PORTFOLIO MOCK] Circuit State: {self.state} | Routing payload.")
        
        if self.state == "OPEN":
            logging.critical("[SRE MOCK] Circuit is OPEN. Fast-failing and caching payload to Redis.")
            return "CACHED_FOR_RETRY"
            
        if downstream_status >= 500 or downstream_status == 408:
            self.consecutive_failures += 1
            logging.warning(f"[SRE MOCK] Downstream failure {self.consecutive_failures}/{self.threshold}")
            
            if self.consecutive_failures >= self.threshold:
                self.state = "OPEN"
                logging.critical("[SRE FATAL] Threshold breached. Tripping Circuit Breaker to OPEN state.")
        else:
            self.consecutive_failures = 0
            
        return "PROCESSED"
