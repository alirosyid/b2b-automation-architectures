import hashlib
import logging
from typing import Optional, Dict

logger = logging.getLogger(__name__)

class DynamicReverseProxy:
    """
    Enterprise API Shield and Caching Layer.
    Masks the underlying n8n orchestrator from external exposure. Intercepts B2B 
    payloads and statefully caches successful workflow outputs to guarantee 
    instant, resilient responses during internal orchestration outages.
    """
    def __init__(self):
        self.response_cache: Dict[str, str] = {}

    def generate_cache_key(self, payload: dict) -> str:
        # Create deterministic hash of the inbound request
        return hashlib.sha256(str(payload).encode()).hexdigest()

    def intercept_and_route(self, payload: dict, backend_status_up: bool) -> str:
        cache_key = self.generate_cache_key(payload)
        
        if not backend_status_up:
            logger.warning("Backend orchestrator offline. Checking local proxy cache.")
            cached_response = self.response_cache.get(cache_key)
            if cached_response:
                logger.info("Proxy served successful historical response. Client SLA maintained.")
                return cached_response
            raise ConnectionError("Backend down and no proxy cache available.")
            
        logger.debug("Backend healthy. Routing traffic normally and updating proxy cache.")
        simulated_backend_response = '{"status": "processed", "id": "1234"}'
        self.response_cache[cache_key] = simulated_backend_response
        return simulated_backend_response
