import logging

logger = logging.getLogger(__name__)

class DynamicPromptOptimizer:
    """
    Self-Improving Algorithmic PromptOps.
    Analyzes historical pipeline failure rates. If structural hallucinations are 
    detected repeatedly, this engine autonomously injects stricter constraints and 
    few-shot examples into the base prompt to mathematically force better LLM behavior.
    """
    def __init__(self):
        self.failure_threshold = 3

    def optimize_prompt(self, base_prompt: str, historical_errors: list) -> str:
        if len(historical_errors) >= self.failure_threshold:
            logger.warning("High failure rate detected. Initiating autonomous prompt optimization.")
            
            optimization_injection = "\n[CRITICAL CONSTRAINTS ADDED AUTONOMOUSLY]:\n"
            if any("json" in err.lower() for err in historical_errors):
                optimization_injection += "- Output MUST be strictly valid JSON. Do not use markdown wrapping (```json).\n"
            
            if any("missing" in err.lower() for err in historical_errors):
                optimization_injection += "- You MUST include all keys defined in the schema, even if the value is null.\n"
                
            optimized_prompt = base_prompt + optimization_injection
            logger.info("Prompt successfully optimized and hardened against historical failures.")
            return optimized_prompt
            
        return base_prompt
