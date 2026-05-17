import re
import logging

logger = logging.getLogger(__name__)

class EdgePIIRedactor:
    """
    Zero-Trust Data Privacy Middleware.
    Intercepts incoming CRM payloads and locally scrubs Personally Identifiable Information (PII)
    prior to transmitting data to third-party LLM APIs (Groq/Gemini).
    """
    PATTERNS = {
        "email": r'[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}',
        "ssn": r'\b\d{3}-\d{2}-\d{4}\b',
        "credit_card": r'\b(?:\d[ -]*?){13,16}\b'
    }

    @classmethod
    def sanitize_payload(cls, raw_text: str) -> str:
        sanitized_text = raw_text
        for data_type, pattern in cls.PATTERNS.items():
            sanitized_text = re.sub(pattern, f"[{data_type.upper()}_REDACTED]", sanitized_text)

        if sanitized_text != raw_text:
            logger.info("PII Redaction Complete: Sensitive corporate data scrubbed at the edge.")
        return sanitized_text
