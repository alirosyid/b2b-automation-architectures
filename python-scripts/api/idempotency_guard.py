import logging
from typing import Optional

logger = logging.getLogger(__name__)

class IdempotencyMiddleware:
    """
    Prevents duplicate API processing and double-billing on network retries.
    Requires clients to send an 'X-Idempotency-Key' header with every webhook.
    """
    def __init__(self):
        self.processed_keys = set()

    def verify_request(self, idempotency_key: Optional[str]) -> bool:
        if not idempotency_key:
            logger.warning("Request rejected: Missing Idempotency Key.")
            return False

        if idempotency_key in self.processed_keys:
            logger.info(f"Idempotency hit for key {idempotency_key}. Returning cached successful response.")
            return False # Halt processing, return 200 OK immediately

        self.processed_keys.add(idempotency_key)
        return True
