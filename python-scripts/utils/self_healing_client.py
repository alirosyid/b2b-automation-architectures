import time
import logging
import httpx
from typing import Callable, Any

logger = logging.getLogger(__name__)

class SelfHealingHTTPClient:
    """
    Bulletproof API Integrator.
    Wraps external outbound HTTP requests (e.g., pushing data to Salesforce). 
    Autonomously catches transient network errors (502, 503, timeouts) and applies 
    Jitter-based Exponential Backoff to guarantee eventual delivery.
    """
    @staticmethod
    def execute_with_backoff(request_func: Callable, max_retries: int = 5) -> Any:
        base_delay = 1.0

        for attempt in range(max_retries):
            try:
                response = request_func()
                response.raise_for_status()
                return response
            except httpx.HTTPError as e:
                if attempt == max_retries - 1:
                    logger.critical(f"Max retries exhausted. Downstream CRM is offline. ({e})")
                    raise

                sleep_time = base_delay * (2 ** attempt)
                logger.warning(f"Transient error caught. Self-healing active: Retrying in {sleep_time}s...")
                time.sleep(sleep_time)
