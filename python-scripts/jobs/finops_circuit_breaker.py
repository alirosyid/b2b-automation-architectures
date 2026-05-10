import logging
from typing import Dict

logger = logging.getLogger(__name__)

class FinOpsCircuitBreaker:
    """
    Monitors dynamic LLM API usage. Trips the circuit (halts processing) 
    if daily burn rate exceeds the predefined B2B client budget.
    """
    def __init__(self, client_budgets: Dict[str, float]):
        self.budgets = client_budgets  # Format: {"client_A": 50.00}
        self.current_spend = {}

    def authorize_llm_call(self, client_id: str, estimated_cost: float) -> bool:
        limit = self.budgets.get(client_id, 5.00) # Default safe limit
        current = self.current_spend.get(client_id, 0.0)

        if current + estimated_cost >= limit:
            logger.critical(f"FinOps Alert: Circuit breaker tripped for {client_id}. Budget exhausted.")
            return False

        self.current_spend[client_id] = current + estimated_cost
        return True
