import time
import logging
from typing import Callable, Any

logger = logging.getLogger(__name__)

class ExternalAPICircuitBreaker:
    """
    Microservice Resilience Architecture.
    Monitors external API health. 'Opens' the circuit after consecutive failures 
    to prevent system bottlenecking, instantly routing payloads to a Dead Letter Queue 
    or fallback mechanism without wasting compute on dead endpoints.
    """
    def __init__(self, failure_threshold: int = 3, recovery_timeout_sec: int = 60):
        self.failure_threshold = failure_threshold
        self.recovery_timeout = recovery_timeout_sec
        self.failure_count = 0
        self.last_failure_time = 0.0
        self.state = "CLOSED"

    def execute_call(self, api_func: Callable, *args, **kwargs) -> Any:
        if self.state == "OPEN":
            if time.time() - self.last_failure_time > self.recovery_timeout:
                logger.info("Circuit Breaker: Attempting 'HALF-OPEN' recovery test.")
                self.state = "HALF-OPEN"
            else:
                logger.warning("Circuit Breaker OPEN: Fast-failing external API request.")
                raise ConnectionAbortedError("Circuit Breaker is OPEN.")
                
        try:
            result = api_func(*args, **kwargs)
            self._reset_circuit()
            return result
        except Exception as e:
            self._record_failure()
            raise e

    def _record_failure(self):
        self.failure_count += 1
        self.last_failure_time = time.time()
        if self.failure_count >= self.failure_threshold:
            self.state = "OPEN"
            logger.critical("Circuit Breaker TRIPPED: External API is down.")

    def _reset_circuit(self):
        self.failure_count = 0
        self.state = "CLOSED"
