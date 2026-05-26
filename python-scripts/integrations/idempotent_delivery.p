import hashlib
import logging

logger = logging.getLogger(__name__)

class IdempotentDeliveryGuard:
    """
    Distributed Systems Reliability layer.
    Generates a cryptographic hash of outgoing CRM payloads. Ensures that 
    aggressive network retries or n8n timeouts do not result in duplicate 
    records or double-billing in the destination system.
    """
    def __init__(self):
        # Production: Distributed Redis Cache
        self.delivered_hashes = set()

    def authorize_delivery(self, payload: dict) -> bool:
        payload_signature = hashlib.sha256(str(payload).encode()).hexdigest()

        if payload_signature in self.delivered_hashes:
            logger.warning("Idempotency Guard hit. Payload already delivered. Blocking duplicate outbound request.")
            return False

        self.delivered_hashes.add(payload_signature)
        logger.info("Idempotency Guard passed. Outbound delivery authorized.")
        return True
