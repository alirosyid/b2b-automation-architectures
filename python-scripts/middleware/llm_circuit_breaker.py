import logging

class LLMCircuitBreaker:
    """
    PORTFOLIO SHOWCASE: API Resiliency Circuit Breaker.
    Prevents cascading failures during upstream LLM provider outages.
    """
    def __init__(self, failure_threshold: int = 3):
        self.failure_threshold = failure_threshold
        self.current_failures = 0
        self.state = "CLOSED" # CLOSED means traffic flows normally

    def execute_request_dry_run(self, primary_api_call_func, fallback_api_call_func):
        if self.state == "OPEN":
            logging.warning("[SRE ALERT] Circuit OPEN. Routing to fallback LLM provider.")
            return fallback_api_call_func()

        try:
            logging.info("[PORTFOLIO MOCK] Attempting primary LLM provider...")
            # Simulating an API failure
            raise ConnectionError("Upstream LLM 502 Bad Gateway")
        except Exception as e:
            self.current_failures += 1
            logging.error(f"[SRE MOCK] Primary API failed: {str(e)}")
            
            if self.current_failures >= self.failure_threshold:
                self.state = "OPEN"
                logging.critical("[SRE CRITICAL] Failure threshold breached. Tripping circuit breaker!")
            
            return fallback_api_call_func()
