import logging

logger = logging.getLogger(__name__)

class AICostGuardrail:
    """
    Enterprise Cost Guardrail: Tracks LLM token usage and prevents API billing overruns.
    Critical for scaling B2B automated outreach without unpredictable expenses.
    """
    
    def __init__(self, monthly_budget_usd: float = 50.0):
        self.monthly_budget = monthly_budget_usd
        self.current_spend = 0.0

    def log_usage(self, model_name: str, prompt_tokens: int, completion_tokens: int) -> float:
        """
        Calculates transaction cost and triggers alerts if nearing budget limits.
        """
        # Dynamic rate approximation (e.g., Groq Llama-3 vs Gemini Flash)
        rate_per_1k = 0.0002 if "llama" in model_name.lower() else 0.0005
        total_tokens = prompt_tokens + completion_tokens
        
        transaction_cost = (total_tokens / 1000) * rate_per_1k
        self.current_spend += transaction_cost
        
        # Business logic alert system
        if self.current_spend >= (self.monthly_budget * 0.9):
            logger.critical(f"🛑 CRITICAL: AI API budget at 90%! Current spend: ${self.current_spend:.2f}")
        elif self.current_spend >= (self.monthly_budget * 0.75):
            logger.warning(f"⚠️ WARNING: AI API budget at 75%. Current spend: ${self.current_spend:.2f}")
            
        logger.info(f"Model: {model_name} | Cost: ${transaction_cost:.5f} | Total API Spend: ${self.current_spend:.4f}")
        
        return transaction_cost

# Example instantiation for the pipeline
# guardrail = AICostGuardrail(monthly_budget_usd=100.0)
