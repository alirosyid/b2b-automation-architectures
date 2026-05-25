import logging
from typing import Callable, List, Dict

logger = logging.getLogger(__name__)

class WaterfallEnrichmentEngine:
    """
    High-Yield B2B Enrichment Cascade.
    Maximizes lead data completion rates by sequentially failing over through 
    a tiered list of API providers if primary data sources return null or error states.
    """
    def __init__(self, provider_chain: List[Callable]):
        self.providers = provider_chain

    def enrich_lead(self, domain: str) -> Dict[str, str]:
        for provider in self.providers:
            try:
                logger.info(f"Attempting enrichment via {provider.__name__}...")
                result = provider(domain)

                if result and result.get("decision_maker_email"):
                    logger.info(f"Enrichment successful via {provider.__name__}.")
                    return result
            except Exception as e:
                logger.warning(f"Provider {provider.__name__} failed ({e}). Cascading...")

        logger.error(f"All enrichment providers exhausted for domain: {domain}.")
        return {"status": "failed_all_providers"}
