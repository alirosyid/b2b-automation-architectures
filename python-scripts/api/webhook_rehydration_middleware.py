import logging
import json
from typing import Dict, Any

logger = logging.getLogger(__name__)

class WebhookRehydrationMiddleware:
    """
    Data Enrichment Edge Architecture.
    Intercepts sparse, ID-only webhooks from upstream CRMs. Synchronously fetches 
    deep relational data from a local state cache (Redis) to 'rehydrate' the payload, 
    delivering fully enriched objects to downstream orchestration nodes.
    """
    def __init__(self, state_cache_client: Any):
        # Production: Configured Redis or Memcached connection
        self.cache = state_cache_client

    def rehydrate_payload(self, sparse_webhook: Dict[str, str]) -> Dict[str, Any]:
        lead_id = sparse_webhook.get("lead_id")
        
        if not lead_id:
            logger.warning("Rehydration bypassed: No valid lead_id in sparse payload.")
            return sparse_webhook
            
        logger.debug(f"Intercepted sparse webhook for {lead_id}. Querying state cache...")
        
        # Simulated high-speed Redis GET
        cached_data_string = self.cache.get(f"b2b_profile:{lead_id}")
        
        if cached_data_string:
            enriched_data = json.loads(cached_data_string)
            # Merge sparse data with rich cached profile
            rehydrated_payload = {**sparse_webhook, **enriched_data, "_rehydrated": True}
            logger.info(f"Payload rehydrated successfully for {lead_id}. Routing to orchestrator.")
            return rehydrated_payload
            
        logger.error(f"Rehydration failed: Lead {lead_id} not found in state cache.")
        return sparse_webhook
