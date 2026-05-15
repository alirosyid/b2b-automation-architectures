import logging

logger = logging.getLogger(__name__)

class ShadowAIMonitor:
    """
    Zero-Trust Corporate Security Tool.
    Scans outbound architectural traffic to detect unauthorized API calls to 
    unapproved LLM endpoints, preventing corporate data exfiltration.
    """
    APPROVED_DOMAINS = ["api.groq.com", "generativelanguage.googleapis.com"]

    @classmethod
    def audit_outbound_request(cls, target_url: str, payload_size_bytes: int):
        domain = target_url.split("/")[2] if "//" in target_url else target_url

        if domain not in cls.APPROVED_DOMAINS:
            logger.critical(f"SECURITY BREACH: Shadow AI usage detected! Unauthorized outbound request to {domain}.")
            # In production: Instantly kill the container network bridge
            return False

        return True
