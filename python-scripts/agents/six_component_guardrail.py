import logging
import re

logger = logging.getLogger(__name__)

class PromptFrameworkGuardrail:
    """
    Enterprise PromptOps Validator.
    Enforces strict compliance with the 6-Component Agent Prompt Framework.
    Blocks outbound LLM execution if the system prompt lacks explicit declarations 
    for Role, Task, Input, Output, Constraints, and Capabilities.
    """
    REQUIRED_COMPONENTS = [
        r"\bRole\b", r"\bTask\b", r"\bInput\b", 
        r"\bOutput\b", r"\bConstraints\b", r"\bCapabilities\b"
    ]

    @classmethod
    def validate_prompt(cls, prompt_text: str) -> bool:
        logger.info("Executing 6-Component structural analysis...")

        for component in cls.REQUIRED_COMPONENTS:
            if not re.search(component, prompt_text, re.IGNORECASE):
                logger.critical(f"Framework Violation: Missing {component}. Halting execution.")
                return False

        logger.info("Validation passed. Prompt is structurally deterministic.")
        return True
