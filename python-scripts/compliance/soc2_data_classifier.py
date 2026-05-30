import logging
import re
from typing import Dict, Any

logger = logging.getLogger(__name__)

class SOC2DataClassifier:
    """
    Real-Time Compliance Automation.
    Scans in-flight JSON payloads and autonomously tags them with strict 
    data classification labels (e.g., PII, PHI, PUBLIC). Ensures enterprise 
    governance and simplifies mandatory SOC2/ISO-27001 auditing processes.
    """
    PII_SIGNATURES = [r'email', r'phone', r'ssn', r'social_security', r'credit_card']

    @classmethod
    def classify_payload(cls, payload: Dict[str, Any]) -> str:
        logger.info("Initializing SOC2 automated data classification scan...")
        payload_string = str(payload).lower()
        
        for signature in cls.PII_SIGNATURES:
            if re.search(signature, payload_string):
                logger.warning(f"Compliance Tag Assigned: SENSITIVE_PII (Signature matched: {signature})")
                return "RESTRICTED_PII"
                
        if "revenue" in payload_string or "financials" in payload_string:
            logger.info("Compliance Tag Assigned: CONFIDENTIAL_FINANCIAL")
            return "CONFIDENTIAL"
            
        logger.debug("Compliance Tag Assigned: STANDARD_BUSINESS")
        return "STANDARD"
