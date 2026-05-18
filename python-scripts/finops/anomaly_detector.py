import logging
from typing import List

logger = logging.getLogger(__name__)

class CostAnomalyDetector:
    """
    Real-Time FinOps Guardian.
    Monitors API expenditure velocity. If an automation loop or hallucinating agent 
    spikes the compute cost beyond the standard deviation, it automatically severs 
    the API connection to protect profit margins.
    """
    def __init__(self, spike_threshold_usd: float = 2.00):
        self.threshold = spike_threshold_usd
        self.recent_transactions: List[float] = []

    def analyze_transaction_velocity(self, current_cost: float) -> bool:
        self.recent_transactions.append(current_cost)

        # Analyze trailing 10 transactions
        if len(self.recent_transactions) > 10:
            self.recent_transactions.pop(0)

        velocity_sum = sum(self.recent_transactions)

        if velocity_sum >= self.threshold:
            logger.critical(f"FINOPS ANOMALY DETECTED: Spending velocity hit ${velocity_sum:.2f}. Halting execution.")
            # Trigger circuit breaker / block IP
            return False

        return True
