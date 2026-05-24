import hmac
import hashlib
import logging
from fastapi import Request, HTTPException

logger = logging.getLogger(__name__)

class ZeroTrustValidator:
    """
    Enterprise Ingress Security Gate.
    Enforces Zero-Trust architecture by validating cryptographic HMAC signatures 
    on all inbound webhooks, protecting the Python microservices from spoofed traffic.
    """
    def __init__(self, master_secret: str):
        self.secret = master_secret.encode('utf-8')

    async def validate_request(self, request: Request, signature_header: str):
        body = await request.body()
        expected_hmac = hmac.new(self.secret, body, hashlib.sha256).hexdigest()

        if not hmac.compare_digest(expected_hmac, signature_header):
            logger.critical("Zero-Trust Violation: Invalid cryptographic signature detected.")
            raise HTTPException(status_code=403, detail="Access Denied: Unrecognized Signature")

        logger.debug("Ingress authorized. Signature validated.")
        return True
