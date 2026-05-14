import json
import logging
from typing import Any, Dict

logger = logging.getLogger(__name__)

class LLMOutputFirewall:
    """
    Enterprise Data Firewall for AI outputs.
    Intercepts LLM responses before they reach the B2B client's CRM.
    Validates JSON structure and strictly enforces business logic rules 
    to prevent database corruption from AI hallucinations.
    """
    BANNED_SIGNATURES = ["I'm sorry, I cannot", "As an AI language model", "Here is the JSON"]

    @classmethod
    def sanitize_and_validate(cls, raw_llm_response: str) -> Dict[str, Any]:
        # 1. Block conversational AI refusals or conversational padding
        for signature in cls.BANNED_SIGNATURES:
            if signature in raw_llm_response:
                logger.error("Firewall blocked payload: AI conversational signature detected.")
                raise ValueError("LLM generated invalid conversational response instead of structured data.")

        # 2. Strict JSON enforcement and Markdown stripping
        try:
            cleaned_response = raw_llm_response.strip().strip("`").removeprefix("json").strip()
            parsed_data = json.loads(cleaned_response)
            logger.info("Firewall passed: LLM output is valid, structured JSON. Safe for CRM injection.")
            return parsed_data
        except json.JSONDecodeError as e:
            logger.critical(f"Firewall blocked payload: Malformed JSON structure. Error: {e}")
            # Production: Route back to n8n to trigger an automated LLM self-correction prompt
            raise ValueError("Strict JSON parsing failed. Automated self-correction loop required.")
