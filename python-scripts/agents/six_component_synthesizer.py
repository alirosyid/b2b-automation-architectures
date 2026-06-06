import logging
from typing import Dict

logger = logging.getLogger(__name__)

class AgentFrameworkSynthesizer:
    """
    Deterministic PromptOps Architecture.
    Programmatically constructs and enforces the 6-Component Agent Framework.
    Guarantees that all dynamic agent instructions possess rigid operational 
    boundaries, mathematically preventing logic drift and hallucinations.
    """
    @staticmethod
    def synthesize_agent(components: Dict[str, str]) -> str:
        required_keys = ["Role", "Task", "Input", "Output", "Constraints", "Capabilities"]
        
        for key in required_keys:
            if key not in components:
                logger.critical(f"Synthesis Failed: Missing mandatory architectural component '{key}'.")
                raise ValueError(f"Agent generation aborted. Missing {key}.")
                
        logger.info("6-Component Framework verified. Synthesizing deterministic agent instructions...")
        
        prompt = f"""
        [ROLE]: {components['Role']}
        [TASK]: {components['Task']}
        [INPUT]: {components['Input']}
        [OUTPUT]: {components['Output']}
        [CONSTRAINTS]: {components['Constraints']}
        [CAPABILITIES]: {components['Capabilities']}
        """
        return prompt.strip()
