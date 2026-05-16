import logging

logger = logging.getLogger(__name__)

class CognitiveComplexityRouter:
    """
    Advanced FinOps routing engine. Analyzes prompt complexity and routes the 
    task to the most cost-efficient LLM, aggressively optimizing API profit margins.
    """
    @staticmethod
    def evaluate_and_route(prompt: str, task_type: str) -> str:
        word_count = len(prompt.split())

        # Simple extraction tasks go to the fastest, cheapest model
        if task_type == "regex_extraction" or word_count < 50:
            logger.info("Low cognitive load detected. Routing to Llama-3 8B (High Speed, Low Cost).")
            return "llama_3_8b_endpoint"

        # Complex reasoning requires the flagship model
        if "analyze" in task_type or word_count > 1000:
            logger.info("High cognitive load detected. Routing to Llama-3 70B (High Accuracy).")
            return "llama_3_70b_endpoint"

        return "default_model_endpoint"
