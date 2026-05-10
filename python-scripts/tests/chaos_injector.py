import random
import logging

logger = logging.getLogger(__name__)

class ChaosMesh:
    """
    Chaos Engineering utility for testing pipeline resilience.
    Randomly simulates API timeouts or database locks in staging environments 
    to verify that exponential backoff and stateful memory recovery work.
    """
    @staticmethod
    def simulate_network_failure(failure_probability: float = 0.05):
        if random.random() < failure_probability:
            logger.critical("CHAOS INJECTED: Simulating catastrophic network timeout.")
            raise ConnectionError("Simulated infrastructure failure.")
        return True
