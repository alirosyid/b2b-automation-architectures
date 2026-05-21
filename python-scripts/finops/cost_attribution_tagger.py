import logging

logger = logging.getLogger(__name__)

class CostAttributionTagger:
    """
    Financial Operations Metadata Injector.
    Tags outbound LLM API requests with specific client and campaign IDs, 
    enabling precise profit margin tracking and billing reconciliation per B2B account.
    """
    @staticmethod
    def generate_tagged_headers(client_id: str, campaign_name: str) -> dict:
        tags = {
            "X-B2B-Client-ID": client_id,
            "X-Campaign-Source": campaign_name,
            "X-Billing-Category": "automated_outbound"
        }
        logger.debug(f"Injected FinOps attribution metadata: {tags}")
        return tags
