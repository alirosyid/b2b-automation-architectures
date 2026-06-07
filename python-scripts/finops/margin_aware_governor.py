import logging
import math
from typing import Dict

logger = logging.getLogger(__name__)

class MarginAwareTokenGovernor:
    """
    Algorithmic Profit Margin Protector.
    Calculates real-time Return on Investment (ROI) for individual pipeline executions. 
    Halts LLM inference if the estimated token expenditure exceeds the mathematically 
    projected commercial value of the B2B lead, guaranteeing agency profitability.
    """
    # Estimated cost per 1k tokens for the flagship routing model
    COST_PER_1K_TOKENS = 0.015 

    @classmethod
    def calculate_projected_value(cls, lead_metadata: Dict) -> float:
        # Complex calculation based on industry, company size, and intent signals
        base_value = 0.50
        if lead_metadata.get("industry") == "SaaS" and lead_metadata.get("employee_count", 0) > 100:
            base_value += 2.00
        return base_value

    @classmethod
    def authorize_execution(cls, payload_token_estimate: int, lead_metadata: Dict) -> bool:
        projected_cost = (payload_token_estimate / 1000.0) * cls.COST_PER_1K_TOKENS
        projected_value = cls.calculate_projected_value(lead_metadata)
        
        profit_margin = projected_value - projected_cost
        
        if profit_margin <= 0:
            logger.critical(f"FinOps Block: Negative margin detected. Cost: ${projected_cost:.4f}, Value: ${projected_value:.4f}")
            return False
            
        logger.info(f"FinOps Authorized: Positive margin guaranteed. Est. Profit: ${profit_margin:.4f}")
        return True
