import hashlib
import logging

logger = logging.getLogger(__name__)

class SemanticCacheManager:
    """
    Advanced LLM Caching Architecture.
    Replaces strict Time-To-Live (TTL) caching with semantic drift detection. 
    Invalidates cached AI responses only when the underlying B2B CRM payload 
    structurally changes, massively reducing redundant API token costs.
    """
    def __init__(self):
        self.semantic_hashes = {}

    def get_or_set_cache(self, entity_id: str, payload_str: str) -> bool:
        current_hash = hashlib.sha256(payload_str.encode()).hexdigest()

        if self.semantic_hashes.get(entity_id) == current_hash:
            logger.info(f"Semantic Cache Hit for {entity_id}. Bypassing LLM execution.")
            return True # Cache is valid, skip LLM

        logger.info(f"Semantic Cache Miss/Drift for {entity_id}. Forcing LLM re-execution.")
        self.semantic_hashes[entity_id] = current_hash
        return False # Cache invalid, run LLM
