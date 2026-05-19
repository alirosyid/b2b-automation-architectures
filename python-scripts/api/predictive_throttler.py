import time
import logging

logger = logging.getLogger(__name__)

class PredictiveThrottler:
    """
    Algorithmic API Traffic Controller.
    Reads incoming rate-limit headers (e.g., X-RateLimit-Remaining) and dynamically 
    applies micro-sleeps to the automation pipeline *before* a 429 error occurs, 
    ensuring buttery-smooth high-volume data ingestion.
    """
    @staticmethod
    def apply_predictive_backoff(remaining_requests: int, reset_time_seconds: int):
        if remaining_requests < 10:
            sleep_duration = (reset_time_seconds / max(remaining_requests, 1)) + 0.1
            logger.warning(f"Approaching API limits. Applying predictive throttle: sleeping for {sleep_duration:.2f}s")
            time.sleep(sleep_duration)
        else:
            logger.debug("API limits healthy. Proceeding at maximum velocity.")
