import logging
import itertools
from typing import List

logger = logging.getLogger(__name__)

class APIKeyLoadBalancer:
    """
    Distributes outbound inference requests across a pool of API keys and providers 
    (e.g., alternating between multiple Groq Llama-3 instances) to bypass 
    strict rate limits during massive B2B data enrichment bursts.
    """
    def __init__(self, key_pool: List[str]):
        self.key_iterator = itertools.cycle(key_pool)

    def get_next_key(self) -> str:
        selected_key = next(self.key_iterator)
        logger.debug(f"Load Balancer: Rotating to API key ending in ...{selected_key[-4:]}")
        return selected_key
