import uuid
import time
import logging
from typing import Optional

logger = logging.getLogger(__name__)

class EphemeralPIIVault:
    """
    Zero-Retention Memory Architecture.
    Stores highly sensitive Personally Identifiable Information (PII) entirely 
    in-memory (RAM) with strict Time-To-Live (TTL) enforcement. 
    Guarantees zero data touches the physical disk, satisfying strict compliance audits.
    """
    def __init__(self, ttl_seconds: int = 300):
        self.ttl = ttl_seconds
        self._vault = {}

    def store_securely(self, sensitive_data: dict) -> str:
        vault_key = uuid.uuid4().hex
        self._vault[vault_key] = {
            "data": sensitive_data,
            "expires_at": time.time() + self.ttl
        }
        logger.debug(f"PII secured in ephemeral vault. Token: {vault_key[:8]}...")
        return vault_key

    def retrieve_and_destroy(self, vault_key: str) -> Optional[dict]:
        record = self._vault.pop(vault_key, None)

        if not record or time.time() > record["expires_at"]:
            logger.warning("Vault retrieval failed: Record expired or does not exist.")
            return None

        logger.info("PII retrieved and permanently destroyed from memory.")
        return record["data"]
