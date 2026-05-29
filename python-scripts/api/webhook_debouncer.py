import time
import hashlib
import json
import logging
from typing import Dict

logger = logging.getLogger(__name__)

class ContextAwareDebouncer:
    """
    High-Frequency Event Optimizer.
    Intercepts rapid-fire identical webhooks (glitches) from upstream B2B CRMs.
    Debounces requests within a temporal window, merging duplicate payloads 
    to prevent redundant n8n executions and save LLM compute costs.
    """
    def __init__(self, debounce_window_sec: float = 2.0):
        self.window = debounce_window_sec
        self.recent_events: Dict[str, float] = {}

    def is_actionable(self, payload: dict) -> bool:
        payload_hash = hashlib.sha256(json.dumps(payload, sort_keys=True).encode()).hexdigest()
        current_time = time.time()
        
        last_seen = self.recent_events.get(payload_hash)
        
        if last_seen and (current_time - last_seen) < self.window:
            logger.info("Debouncer active: Ignored duplicate high-frequency webhook.")
            self.recent_events[payload_hash] = current_time # Reset timer
            return False
            
        self.recent_events[payload_hash] = current_time
        logger.debug("Debouncer passed. Payload cleared for orchestration.")
        return True
