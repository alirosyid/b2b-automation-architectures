class SaaSThrottler:
    """
    Monetization infrastructure: Applies dynamic rate limiting based on the 
    client's subscription tier to protect server capacity and enforce billing structures.
    """
    TIER_LIMITS = {
        "basic": 10,       # reqs per minute
        "pro": 50,
        "enterprise": 500
    }

    @classmethod
    def check_rate_limit(cls, client_tier: str, current_req_count: int) -> bool:
        max_requests = cls.TIER_LIMITS.get(client_tier.lower(), 5)

        if current_req_count >= max_requests:
            return False # Rate limit exceeded
        return True
