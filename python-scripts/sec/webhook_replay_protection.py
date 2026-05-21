import time
import logging
from typing import Set

logger = logging.getLogger(__name__)

class ReplayProtectionGuard:
    """
    Zero-Trust Ingress Firewall.
    Mitigates cryptographic replay attacks by tracking webhook message IDs 
    and enforcing strict temporal windows for payload validity.
    """
    def __init__(self, temporal_window_seconds: int = 300):
        self.window = temporal_window_seconds
        self.processed_nonces: Set[str] = set()

    def validate_request(self, message_id: str, timestamp: int) -> bool:
        current_time = int(time.time())

        if abs(current_time - timestamp) > self.window:
            logger.critical("Security Breach: Request timestamp falls outside valid temporal window.")
            return False

        if message_id in self.processed_nonces:
            logger.critical("Security Breach: Replay attack detected. Message ID already processed.")
            return False

        self.processed_nonces.add(message_id)
        return True
