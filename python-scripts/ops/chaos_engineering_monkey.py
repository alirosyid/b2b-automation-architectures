import logging
import random
import time

logger = logging.getLogger(__name__)

class ChaosEngineeringMonkey:
    """
    SRE Resilience Testing Tool.
    Intentionally injects randomized transient faults (timeouts, 502s, rate limits) 
    into staging pipelines. Validates that the architecture's self-healing 
    and Dead Letter Queue (DLQ) mechanisms function perfectly under extreme duress.
    """
    def __init__(self, failure_probability: float = 0.05):
        self.probability = failure_probability

    def execute_chaos_simulation(self):
        chance = random.random()
        
        if chance < self.probability:
            fault_type = random.choice(["LATENCY", "HTTP_502", "CONNECTION_RESET"])
            
            if fault_type == "LATENCY":
                logger.warning("[CHAOS MONKEY] Simulating severe network degradation. Sleeping 10s...")
                time.sleep(10)
            elif fault_type == "HTTP_502":
                logger.error("[CHAOS MONKEY] Simulating catastrophic upstream gateway failure (502).")
                raise ConnectionError("Simulated Upstream API Failure")
            elif fault_type == "CONNECTION_RESET":
                logger.error("[CHAOS MONKEY] Simulating TCP Connection Reset.")
                raise BrokenPipeError("Simulated TCP Drop")
                
        logger.debug("[CHAOS MONKEY] Execution passed. System operating normally.")
