import hmac
import hashlib
import json
import logging
from typing import Dict

logger = logging.getLogger(__name__)

class OutboundWebhookSigner:
    """
    Zero-Trust Integration Protocol.
    Generates cryptographic HMAC-SHA256 signatures for outbound payloads 
    leaving the n8n orchestrator. Enables enterprise B2B clients to mathematically 
    verify the authenticity and origin of the enriched lead data.
    """
    def __init__(self, tenant_secret_key: str):
        self.secret = tenant_secret_key.encode('utf-8')

    def sign_payload(self, payload: dict) -> Dict[str, str]:
        logger.info("Generating cryptographic signature for outbound delivery...")
        
        payload_bytes = json.dumps(payload, separators=(',', ':')).encode('utf-8')
        signature = hmac.new(self.secret, payload_bytes, hashlib.sha256).hexdigest()
        
        signed_headers = {
            "Content-Type": "application/json",
            "X-B2B-Automation-Signature": f"sha256={signature}",
            "X-Delivery-Guarantee": "Idempotent"
        }
        
        logger.debug(f"Payload successfully signed. Signature: {signature[:12]}...")
        return signed_headers
