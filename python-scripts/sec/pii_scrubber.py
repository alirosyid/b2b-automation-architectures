import re
import logging

logger = logging.getLogger(__name__)

class DataLossPrevention:
    """
    Enterprise DLP Middleware. Scrubs sensitive B2B data (PII) 
    before it is transmitted to external LLM providers to ensure GDPR compliance.
    """
    @staticmethod
    def mask_sensitive_data(text: str) -> str:
        # Mask emails
        text = re.sub(r'[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}', '[REDACTED_EMAIL]', text)
        # Mask standard phone numbers
        text = re.sub(r'\b\d{3}[-.]?\d{3}[-.]?\d{4}\b', '[REDACTED_PHONE]', text)
        logger.info("DLP Check Complete: PII masked successfully.")
        return text
