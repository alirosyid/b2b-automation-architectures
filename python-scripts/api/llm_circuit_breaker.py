import time

class CircuitBreaker:
    def __init__(self, failure_threshold=3, recovery_timeout=60):
        self.failure_threshold = failure_threshold
        self.recovery_timeout = recovery_timeout
        self.failures = 0
        self.state = "CLOSED"
        self.last_failure_time = None

    def execute_call(self, api_function, *args, **kwargs):
        if self.state == "OPEN":
            if time.time() - self.last_failure_time > self.recovery_timeout:
                self.state = "HALF_OPEN"
            else:
                return {"error": "Circuit Breaker OPEN. Request blocked to prevent cascading failure."}

        try:
            result = api_function(*args, **kwargs)
            self._reset()
            return result
        except Exception as e:
            self._record_failure()
            return {"error": f"API Call Failed: {str(e)}"}

    def _record_failure(self):
        self.failures += 1
        self.last_failure_time = time.time()
        if self.failures >= self.failure_threshold:
            self.state = "OPEN"
            print("[SRE] CRITICAL: Circuit Breaker TRIPPED. Halting outbound requests.")

    def _reset(self):
        self.failures = 0
        self.state = "CLOSED"
