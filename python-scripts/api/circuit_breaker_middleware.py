class CircuitBreaker:
    def __init__(self, failure_threshold=3, recovery_timeout=60):
        self.failure_threshold = failure_threshold
        self.recovery_timeout = recovery_timeout
        self.failures = 0
        self.state = "CLOSED" # CLOSED, OPEN, HALF_OPEN
        self.last_failure_time = None

    def execute(self, api_call_function, fallback_function):
        if self.state == "OPEN":
            import time
            if time.time() - self.last_failure_time > self.recovery_timeout:
                print("[Circuit Breaker] State HALF_OPEN. Testing external API recovery...")
                self.state = "HALF_OPEN"
            else:
                print("[Circuit Breaker] State OPEN. Rerouting to fallback provider immediately.")
                return fallback_function()
                
        try:
            result = api_call_function()
            self.failures = 0
            self.state = "CLOSED"
            return result
        except Exception as e:
            self.failures += 1
            print(f"[!] API Failure. Strike {self.failures}/{self.failure_threshold}")
            if self.failures >= self.failure_threshold:
                self.state = "OPEN"
                self.last_failure_time = time.time()
                print("[!] 🛑 CIRCUIT TRIPPED. External API isolated to protect core infrastructure.")
            return fallback_function()
