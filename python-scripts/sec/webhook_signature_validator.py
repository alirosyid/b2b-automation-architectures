import hmac
import hashlib
import logging

logger = logging.getLogger(__name__)

class WebhookSignatureValidator:
    """
    Zero-Trust Edge Security Gateway.
    Protects downstream orchestration and LLM infrastructure from unauthorized ingress. 
    Mathematically validates cryptographic HMAC-SHA256 signatures on inbound payloads, 
    instantly dropping unverified traffic to prevent FinOps exploitation.
    """
    def __init__(self, master_secret: str):
        self.secret = master_secret.encode('utf-8')

    def verify_ingress(self, raw_payload_bytes: bytes, provided_signature: str) -> bool:
        logger.debug("Executing cryptographic HMAC validation on inbound webhook...")
        
        expected_signature = hmac.new(self.secret, raw_payload_bytes, hashlib.sha256).hexdigest()
        
        if not hmac.compare_digest(expected_signature, provided_signature):
            logger.critical("Zero-Trust Violation: Invalid payload signature. Dropping connection.")
            return False
            
        logger.info("Ingress authorized. Cryptographic signature verified.")
        return True
