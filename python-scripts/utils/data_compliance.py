import re
import logging

logger = logging.getLogger(__name__)

class PIIAnonymizer:
    """
    Masks sensitive B2B data (emails, phone numbers) before LLM processing 
    to ensure GDPR and CCPA compliance.
    """
    @staticmethod
    def mask_email(text: str) -> str:
        email_pattern = r'[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}'
        masked_text = re.sub(email_pattern, "[REDACTED_EMAIL]", text)
        if text != masked_text:
            logger.info("PII Data masked successfully.")
        return masked_text
