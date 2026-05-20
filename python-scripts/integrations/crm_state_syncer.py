import hashlib
import json
import logging

logger = logging.getLogger(__name__)

class CRMStateSyncer:
    """
    Eventual Consistency Guardian.
    Maintains a local cryptographic hash of remote CRM states. Prevents infinite 
    bidirectional webhook loops by ensuring outbound API mutations are only 
    fired when genuine data divergence is mathematically proven.
    """
    def __init__(self):
        self.state_hashes = {}

    def push_update_if_divergent(self, record_id: str, payload: dict) -> bool:
        payload_hash = hashlib.sha256(json.dumps(payload, sort_keys=True).encode()).hexdigest()

        if self.state_hashes.get(record_id) == payload_hash:
            logger.debug(f"State sync bypassed: Record {record_id} is already consistent.")
            return False # Do not trigger API

        logger.info(f"State divergence detected for {record_id}. Executing CRM mutation.")
        self.state_hashes[record_id] = payload_hash
        # Production: Execute HTTP PATCH to CRM
        return True
