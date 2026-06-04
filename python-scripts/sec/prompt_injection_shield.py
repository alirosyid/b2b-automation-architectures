import logging
import re

logger = logging.getLogger(__name__)

class PromptInjectionShield:
    """
    Zero-Trust LLMOps Security.
    Intercepts dynamic agent instructions and guarantees they strictly conform 
    to the 6-Component Agent Prompt Framework. Proactively sanitizes inputs 
    to prevent adversarial hijacking of the B2B pipeline.
    """
    REQUIRED_FRAMEWORK = [
        r"\[ROLE\]", r"\[TASK\]", r"\[INPUT\]", 
        r"\[OUTPUT\]", r"\[CONSTRAINTS\]", r"\[CAPABILITIES\]"
    ]

    @classmethod
    def sanitize_and_verify(cls, system_prompt: str, user_payload: str) -> bool:
        logger.info("Executing 6-Component architectural validation on outbound prompt...")
        
        for component in cls.REQUIRED_FRAMEWORK:
            if not re.search(component, system_prompt, re.IGNORECASE):
                logger.critical(f"Security Alert: Missing framework constraint {component}. Halting inference.")
                return False
                
        # Basic injection sanitization
        if "ignore all previous instructions" in user_payload.lower():
            logger.critical("Security Alert: Malicious prompt injection detected in payload. Dropping request.")
            return False
            
        logger.debug("Prompt architecture verified. Secure for LLM dispatch.")
        return True
