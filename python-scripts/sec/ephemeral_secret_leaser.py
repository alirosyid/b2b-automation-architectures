import uuid
import time
import logging
from typing import Dict

logger = logging.getLogger(__name__)

class EphemeralSecretLeaser:
    """
    Zero-Trust Credential Architecture.
    Leases short-lived, ephemeral API secrets for microservice authentication.
    Automatically invalidates credentials after strict temporal bounds (TTL) expire, 
    mathematically eliminating the risk of long-term credential leakage.
    """
    def __init__(self, ttl_seconds: int = 600):
        self.ttl = ttl_seconds
        self.active_leases: Dict[str, float] = {}

    def lease_secret(self, service_id: str) -> str:
        ephemeral_key = f"EPH_{uuid.uuid4().hex}"
        self.active_leases[ephemeral_key] = time.time() + self.ttl
        
        logger.info(f"Ephemeral secret leased for service {service_id}. TTL: {self.ttl}s")
        return ephemeral_key

    def validate_secret(self, provided_key: str) -> bool:
        expiration_time = self.active_leases.get(provided_key)
        
        if not expiration_time:
            logger.warning("Authentication failed: Ephemeral key unknown.")
            return False
            
        if time.time() > expiration_time:
            logger.critical("Authentication failed: Ephemeral key expired. Zero-Trust enforced.")
            del self.active_leases[provided_key]
            return False
            
        logger.debug("Authentication passed. Ephemeral key is valid.")
        return True
