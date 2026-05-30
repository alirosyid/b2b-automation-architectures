import logging
import re

logger = logging.getLogger(__name__)

class PromptInjectionHoneypot:
    """
    Agentic Cyber Defense Mechanism.
    Scans inbound B2B textual payloads for known prompt-injection vectors 
    (e.g., DAN, 'ignore previous instructions'). Quarantines malicious payloads 
    instantly to protect downstream LLM orchestration from unauthorized hijacking.
    """
    MALICIOUS_VECTORS = [
        r"(?i)ignore all previous",
        r"(?i)disregard the above",
        r"(?i)system prompt",
        r"(?i)you are now completely free"
    ]

    @classmethod
    def scan_payload(cls, user_input: str) -> bool:
        logger.debug("Executing proactive prompt-injection scan on inbound payload...")
        
        for vector in cls.MALICIOUS_VECTORS:
            if re.search(vector, user_input):
                logger.critical(f"SECURITY BREACH DETECTED: Malicious prompt-injection vector identified -> '{vector}'")
                # Production: Route to isolated honeypot logging system, drop actual request
                return False
                
        logger.info("Payload cleared by Honeypot. No injection vectors detected.")
        return True
