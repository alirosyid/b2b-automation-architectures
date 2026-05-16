import logging

logger = logging.getLogger(__name__)

class RevenueAttributionEngine:
    """
    Closes the loop between automation execution and closed-won revenue.
    Injects tracking metadata into AI-processed leads to prove direct 
    financial ROI to enterprise Chief Financial Officers (CFOs).
    """
    @staticmethod
    def tag_lead_for_attribution(lead_data: dict, campaign_id: str) -> dict:
        attribution_tag = f"ai_pipeline_{campaign_id}"
        lead_data["utm_automation_source"] = attribution_tag

        logger.info(f"Lead {lead_data.get('email')} tagged with attribution ID: {attribution_tag}")
        return lead_data

    @staticmethod
    def calculate_pipeline_roi(closed_deals_from_crm: list) -> dict:
        total_revenue = sum(deal["amount"] for deal in closed_deals_from_crm if "ai_pipeline" in deal.get("source", ""))
        logger.info(f"Verified Automation ROI: ${total_revenue:,.2f} in closed-won revenue.")
        return {"attributed_revenue_usd": total_revenue}
