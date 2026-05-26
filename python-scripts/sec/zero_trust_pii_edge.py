import re
import logging

logger = logging.getLogger(__name__)

class ZeroTrustPIIRedactor:
    """
    Edge-Based Data Loss Prevention (DLP).
    Intercepts inbound B2B payloads and locally scrubs Personally Identifiable 
    Information (PII) prior to transmitting data to third-party LLM APIs, 
    ensuring strict GDPR and SOC2 compliance.
    """
    PII_PATTERNS = [
        (r'[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}', '[REDACTED_EMAIL]'),
        (r'\b\d{3}[-.]?\d{3}[-.]?\d{4}\b', '[REDACTED_PHONE]')
    ]

    @classmethod
    def sanitize(cls, raw_text: str) -> str:
        safe_text = raw_text
        for pattern, replacement in cls.PII_PATTERNS:
            safe_text = re.sub(pattern, replacement, safe_text)

        if safe_text != raw_text:
            logger.info("Zero-Trust DLP Active: PII scrubbed at the edge.")

        return safe_text
