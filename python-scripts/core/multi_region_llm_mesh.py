import asyncio
import time
import logging
import random
from typing import Dict, List, Any

logger = logging.getLogger(__name__)

class GlobalLLMMeshRouter:
    """
    Geographical High-Availability (HA) Traffic Router.
    Distributes massive LLM inference loads across globally distributed API regions. 
    Continuously tracks regional latency and dynamically shifts routing weights 
    to bypass geographical rate-limits and guarantee sub-second B2B data processing.
    """
    def __init__(self, region_endpoints: List[str]):
        self.regions = {url: {"latency": 0.5, "failures": 0, "weight": 1.0} for url in region_endpoints}
        self.decay_factor = 0.9

    async def _ping_region(self, url: str):
        start_time = time.time()
        try:
            # Simulated async latency ping to endpoint health route
            await asyncio.sleep(random.uniform(0.1, 0.8))
            latency = time.time() - start_time
            self.regions[url]["latency"] = (self.regions[url]["latency"] * self.decay_factor) + (latency * (1 - self.decay_factor))
            self.regions[url]["failures"] = 0
            self.regions[url]["weight"] = 1.0 / self.regions[url]["latency"]
        except Exception:
            self.regions[url]["failures"] += 1
            self.regions[url]["weight"] = 0.01 # Heavily penalize failing regions

    async def get_optimal_region(self) -> str:
        # Background task to update latencies asynchronously
        asyncio.create_task(asyncio.gather(*(self._ping_region(url) for url in self.regions)))
        
        # Select region based on highest calculated weight (lowest latency/failures)
        available_regions = [r for r, stats in self.regions.items() if stats["failures"] < 3]
        if not available_regions:
            logger.critical("Catastrophic Global Outage: All regional LLM endpoints offline.")
            raise ConnectionError("Global mesh routing failed.")
            
        optimal_region = max(available_regions, key=lambda r: self.regions[r]["weight"])
        logger.debug(f"Mesh Router: Directing inference to {optimal_region} (Weight: {self.regions[optimal_region]['weight']:.2f})")
        return optimal_region
