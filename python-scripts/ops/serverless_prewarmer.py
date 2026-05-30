import httpx
import asyncio
import logging
from typing import List

logger = logging.getLogger(__name__)

class ServerlessPrewarmer:
    """
    Sub-Millisecond Latency Optimization.
    Executes lightweight periodic pings against critical serverless AI endpoints 
    (e.g., AWS Lambda, GCP Cloud Run). Prevents container 'cold starts', 
    guaranteeing ultra-low latency for synchronous B2B webhook responses.
    """
    def __init__(self, target_endpoints: List[str]):
        self.endpoints = target_endpoints

    async def execute_warming_cycle(self):
        logger.info("Initializing serverless pre-warming protocol...")
        
        async with httpx.AsyncClient(timeout=3.0) as client:
            tasks = []
            for url in self.endpoints:
                # Dispatching minimal HEAD requests to wake idle containers
                tasks.append(client.head(url, headers={"X-Prewarm-Ping": "true"}))
                
            results = await asyncio.gather(*tasks, return_exceptions=True)
            
            for url, result in zip(self.endpoints, results):
                if isinstance(result, Exception):
                    logger.warning(f"Pre-warm failed for {url}: {result}")
                else:
                    logger.debug(f"Endpoint {url} successfully warmed. Status: {result.status_code}")
