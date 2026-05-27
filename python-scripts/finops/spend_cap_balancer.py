import logging
import time

logger = logging.getLogger(__name__)

class SpendCapLoadBalancer:
    """
    Strict FinOps Governor.
    Tracks aggregate LLM API expenditure in real-time. Dynamically cascades 
    traffic to lower-cost open-source models once hourly enterprise budget 
    ceilings are mathematically breached.
    """
    def __init__(self, hourly_budget_usd: float = 5.00):
        self.budget = hourly_budget_usd
        self.current_spend = 0.0
        self.window_start = time.time()

    def route_inference(self, estimated_cost: float) -> str:
        if time.time() - self.window_start > 3600:
            self.current_spend = 0.0
            self.window_start = time.time()
            
        if self.current_spend + estimated_cost > self.budget:
            logger.warning(f"FinOps Threshold Reached (${self.current_spend:.2f}/${self.budget}). Cascading to Economy Tier.")
            return "economy_local_vllm_endpoint"
            
        self.current_spend += estimated_cost
        logger.debug(f"Budget healthy. Routing to Premium Tier. Current Spend: ${self.current_spend:.2f}")
        return "premium_flagship_endpoint"
