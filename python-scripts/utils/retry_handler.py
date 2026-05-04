import time
import logging
from functools import wraps

logger = logging.getLogger(__name__)

def retry_with_backoff(retries=3, backoff_in_seconds=2):
    """
    Decorator to retry transient API failures in automated workflows.
    Critical for maintaining pipeline stability.
    """
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            x = 0
            while True:
                try:
                    return func(*args, **kwargs)
                except Exception as e:
                    if x == retries:
                        logger.error(f"Failed after {retries} retries: {e}")
                        raise
                    sleep_time = (backoff_in_seconds * 2 ** x)
                    logger.warning(f"Attempt {x+1} failed. Retrying in {sleep_time}s...")
                    time.sleep(sleep_time)
                    x += 1
        return wrapper
    return decorator
