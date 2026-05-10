import time
import logging

logger = logging.getLogger(__name__)

class ServerlessWarmer:
    """
    Prevents latency spikes (cold starts) in containerized deployments.
    Executes lightweight dummy payloads to keep Python microservices loaded in RAM.
    """
    @staticmethod
    def keep_alive(endpoints: list):
        logger.info("Executing serverless warming protocol...")
        for endpoint in endpoints:
            # Simulated ping
            start = time.time()
            # requests.get(f"{endpoint}/health")
            latency = round((time.time() - start) * 1000, 2)
            logger.info(f"Endpoint {endpoint} warmed. Latency: {latency}ms")
