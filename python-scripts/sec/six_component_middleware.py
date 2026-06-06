import logging
import re
from typing import Dict

logger = logging.getLogger(__name__)

class SixComponentMiddleware:
    """
    Deterministic PromptOps & Security Gateway.
    Programmatically enforces the 6-Component Agent Framework while actively 
    scanning for adversarial prompt injection vectors (e.g., 'ignore previous').
    """
    MALICIOUS_VECTORS = [r"(?i)ignore all previous", r"(?i)disregard the above", r"(?i)system prompt"]

    @classmethod
    def synthesize_and_secure(cls, raw_task: str, expected_schema: str, payload: str) -> str:
        logger.info("Executing 6-Component synthesis and security scan...")
        
        for vector in cls.MALICIOUS_VECTORS:
            if re.search(vector, payload):
                logger.critical(f"Security Alert: Malicious prompt injection detected. Halting.")
                raise PermissionError("Adversarial payload intercepted by middleware.")

        prompt = f"""
        [ROLE]: Enterprise B2B Data Architect.
        [TASK]: {raw_task}
        [INPUT]: {payload}
        [OUTPUT]: Strictly formatted JSON matching this schema: {expected_schema}.
        [CONSTRAINTS]: No conversational padding. No markdown wrapping. Output only valid JSON.
        [CAPABILITIES]: You have access to semantic extraction and logical inference.
        """
        
        logger.debug("Prompt synthesis complete. Deterministic guardrails applied.")
        return prompt.strip()
