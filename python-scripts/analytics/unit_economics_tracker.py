import logging

logger = logging.getLogger(__name__)

class AIUnitEconomicsTracker:
    """
    Bridges Engineering and Finance. 
    Calculates the true Customer Acquisition Cost (CAC) by merging LLM API 
    token expenditures with CRM conversion data to prove exact business ROI.
    """
    def __init__(self):
        self.campaign_costs = {}

    def log_token_expenditure(self, campaign_id: str, cost_usd: float):
        if campaign_id not in self.campaign_costs:
            self.campaign_costs[campaign_id] = 0.0
        self.campaign_costs[campaign_id] += cost_usd

    def calculate_campaign_roi(self, campaign_id: str, closed_deals: int, avg_deal_size: float) -> dict:
        total_api_cost = self.campaign_costs.get(campaign_id, 0.0)
        gross_revenue = closed_deals * avg_deal_size

        cost_per_acquisition = total_api_cost / closed_deals if closed_deals > 0 else total_api_cost

        logger.info(f"Unit Economics for {campaign_id} -> Cost per Deal: ${cost_per_acquisition:.2f}")

        return {
            "campaign_id": campaign_id,
            "total_ai_compute_cost": total_api_cost,
            "gross_revenue_generated": gross_revenue,
            "ai_cost_per_acquisition": cost_per_acquisition
        }
