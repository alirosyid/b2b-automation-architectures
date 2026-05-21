import logging

logger = logging.getLogger(__name__)

class SemanticIntentRouter:
    """
    Lightweight Edge AI Router.
    Classifies incoming unstructured text (e.g., inbound emails) into distinct 
    business intents, routing the payload to highly specialized n8n sub-workflows 
    for optimal automated handling.
    """
    INTENT_ROUTES = {
        "sales_inquiry": "https://n8n.internal/webhook/sales-agent",
        "support_ticket": "https://n8n.internal/webhook/support-agent",
        "spam": "drop_payload"
    }

    @classmethod
    def route_payload(cls, text_content: str) -> str:
        # Simulated fast local classification (e.g., using a small sentence-transformer)
        if "pricing" in text_content.lower() or "demo" in text_content.lower():
            logger.info("Intent Classified: Sales Inquiry. Routing to Sales Agent Swarm.")
            return cls.INTENT_ROUTES["sales_inquiry"]

        return cls.INTENT_ROUTES["support_ticket"]
