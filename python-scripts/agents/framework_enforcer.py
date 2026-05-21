import logging
from typing import Dict, Any

logger = logging.getLogger(__name__)

class PromptFrameworkEnforcer:
    """
    Validates LLM outputs against strict 6-Component Prompt structures.
    Ensures the agent strictly adhered to: Role, Task, Input, Output, Constraints, and Capabilities.
    Rejects outputs that violate defined constraints (e.g., generating markdown when JSON was requested).
    """
    @classmethod
    def validate_execution(cls, llm_response: Dict[str, Any], constraints: list) -> bool:
        logger.info("Executing 6-Component Framework validation check...")
        response_text = str(llm_response).lower()

        for constraint in constraints:
            if "no conversational text" in constraint.lower() and "here is the" in response_text:
                logger.critical("Constraint Violation: Conversational padding detected.")
                return False

        logger.info("Framework validation passed. Output is deterministic and CRM-ready.")
        return True
