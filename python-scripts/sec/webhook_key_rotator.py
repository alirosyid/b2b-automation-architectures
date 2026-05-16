import hmac
import hashlib
import logging
from typing import List

logger = logging.getLogger(__name__)

class ZeroDowntimeKeyRotator:
    """
    Allows seamless, zero-downtime cryptographic key rotation for B2B webhooks.
    Maintains a rolling window of active secrets, ensuring CRM webhooks do not 
    fail during the transition period between old and new API keys.
    """
    def __init__(self, active_secrets: List[str]):
        self.valid_secrets = [secret.encode() for secret in active_secrets]

    def validate_signature(self, payload_body: bytes, provided_signature: str) -> bool:
        for secret in self.valid_secrets:
            expected = hmac.new(secret, payload_body, hashlib.sha256).hexdigest()
            if hmac.compare_digest(expected, provided_signature):
                logger.debug("Signature validated against active key vault.")
                return True

        logger.warning("Signature validation failed across all active keys in the rotation window.")
        return False
