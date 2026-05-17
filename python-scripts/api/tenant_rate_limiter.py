import time
import logging

logger = logging.getLogger(__name__)

class TokenBucketRateLimiter:
    """
    Enterprise SaaS Gateway. Implements the Token Bucket algorithm to enforce 
    strict rate limits per B2B tenant, preventing 'noisy neighbor' server crashes 
    and protecting global pipeline throughput.
    """
    def __init__(self, capacity: int, refill_rate_per_sec: float):
        self.capacity = capacity
        self.refill_rate = refill_rate_per_sec
        self.tenants = {} # Maps tenant_id to {"tokens": float, "last_refill": float}

    def consume(self, tenant_id: str, tokens_required: int = 1) -> bool:
        now = time.time()
        if tenant_id not in self.tenants:
            self.tenants[tenant_id] = {"tokens": self.capacity, "last_refill": now}

        tenant_data = self.tenants[tenant_id]
        time_passed = now - tenant_data["last_refill"]

        # Refill tokens based on time elapsed
        tenant_data["tokens"] = min(self.capacity, tenant_data["tokens"] + time_passed * self.refill_rate)
        tenant_data["last_refill"] = now

        if tenant_data["tokens"] >= tokens_required:
            tenant_data["tokens"] -= tokens_required
            return True

        logger.warning(f"Rate Limit Exceeded: Tenant {tenant_id} throttled (HTTP 429).")
        return False
