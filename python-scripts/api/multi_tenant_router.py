import logging
from fastapi import Request, HTTPException

logger = logging.getLogger(__name__)

class MultiTenantWebhookRouter:
    """
    SaaS Master Ingress Node.
    Provides a single, unified webhook endpoint for all B2B clients. 
    Dynamically analyzes the authorization header and intelligently routes 
    the payload to the specific tenant's isolated n8n pipeline in the backend.
    """
    # Simulated database mapping API keys to specific n8n workflows
    TENANT_MAP = {
        "sk_client_alpha_99": "https://n8n.internal/webhook/tenant-alpha-flow",
        "sk_client_beta_42": "https://n8n.internal/webhook/tenant-beta-flow"
    }

    @classmethod
    def route_inbound_traffic(cls, request: Request, api_key: str) -> str:
        target_webhook = cls.TENANT_MAP.get(api_key)

        if not target_webhook:
            logger.critical("Unauthorized ingress attempt: Invalid or revoked API key.")
            raise HTTPException(status_code=401, detail="Unauthorized Tenant")

        logger.info(f"Tenant authenticated. Routing traffic to isolated pipeline: {target_webhook}")
        return target_webhook
