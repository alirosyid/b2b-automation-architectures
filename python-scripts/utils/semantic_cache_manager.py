class SemanticCacheManager:
    """
    Advanced LLM caching mechanism. Instead of strict time-to-live (TTL),
    it evaluates if the underlying context has drifted semantically before invalidating the cache.
    """
    def __init__(self):
        self.cache_registry = {}

    def invalidate_if_stale(self, entity_id: str, new_context_hash: str) -> bool:
        stored_hash = self.cache_registry.get(entity_id)

        if stored_hash != new_context_hash:
            # Semantic drift detected, force cache invalidation
            self.cache_registry.pop(entity_id, None)
            return True
        return False
