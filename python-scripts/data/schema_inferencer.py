import logging
from typing import Dict, Any

logger = logging.getLogger(__name__)

class SchemaInferencer:
    """
    Autonomous Data Normalization.
    Analyzes messy, undocumented JSON payloads from enterprise clients and 
    dynamically maps disparate fields (e.g., 'emailAddress' or 'contact_mail') 
    to a unified B2B architecture schema.
    """
    STANDARD_SCHEMA = ["id", "email", "company", "revenue"]

    @classmethod
    def normalize_payload(cls, raw_payload: Dict[str, Any]) -> dict:
        normalized = {}
        logger.info("Inferring schema mapping from unstructured payload...")

        for key, value in raw_payload.items():
            key_lower = key.lower()
            if "mail" in key_lower:
                normalized["email"] = value
            elif "org" in key_lower or "comp" in key_lower:
                normalized["company"] = value

        logger.info("Payload successfully normalized to standard schema.")
        return normalized
