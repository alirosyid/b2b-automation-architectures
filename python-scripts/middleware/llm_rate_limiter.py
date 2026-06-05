import time
import logging

logger = logging.getLogger(__name__)

class LLMRateLimiter:
    """
    Manages API call frequencies to comply with provider rate limits.
    Implements exponential backoff for HTTP 429 (Too Many Requests) errors.
    """
    @staticmethod
    def execute_with_backoff(func, max_retries: int = 3, base_delay: float = 2.0, *args, **kwargs):
        for attempt in range(max_retries):
            try:
                return func(*args, **kwargs)
            except Exception as e:
                if "429" in str(e) or "Too Many Requests" in str(e):
                    sleep_time = base_delay * (2 ** attempt)
                    logger.warning(f"Rate limit hit. Retrying in {sleep_time}s (Attempt {attempt + 1}/{max_retries})")
                    time.sleep(sleep_time)
                else:
                    raise e
        logger.error("Max retries exceeded for LLM API call.")
        raise Exception("Rate limit backoff failed.")
