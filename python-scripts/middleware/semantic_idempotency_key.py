import logging
import hashlib
import json

class SemanticIdempotencyGuard:
    """
    PORTFOLIO SHOWCASE: Distributed System Idempotency.
    Generates semantic hashes to drop duplicate B2B webhooks at the edge layer.
    """
    def __init__(self):
        self.processed_keys = set() # Mock Redis cache

    def evaluate_payload_dry_run(self, raw_payload: dict) -> bool:
        logging.info("[PORTFOLIO MOCK] Generating semantic idempotency key...")
        
        # Strip timestamps or trace IDs that change between retries
        semantic_data = {k: v for k, v in raw_payload.items() if k not in ["timestamp", "trace_id"]}
        serialized = json.dumps(semantic_data, sort_keys=True).encode('utf-8')
        idempotency_key = hashlib.sha256(serialized).hexdigest()
        
        if idempotency_key in self.processed_keys:
            logging.warning(f"[DATA ENG ALERT] Duplicate semantic payload detected ({idempotency_key}). Dropping at edge.")
            return False
            
        self.processed_keys.add(idempotency_key)
        logging.info("[DATA ENG MOCK] Unique payload verified. Proceeding to extraction.")
        return True
