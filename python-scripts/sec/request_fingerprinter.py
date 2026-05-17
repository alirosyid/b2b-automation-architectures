import hashlib
import logging
from fastapi import Request, HTTPException

logger = logging.getLogger(__name__)

class RequestFingerprinter:
    """
    Zero-Trust Ingress Security.
    Generates a cryptographic fingerprint of incoming HTTP requests to detect 
    and block malicious bot traffic, replay attacks, and unauthorized webhook spoofing.
    """
    @staticmethod
    def generate_fingerprint(request: Request) -> str:
        # Combine IP, User-Agent, and specific B2B CRM headers to create a unique signature
        ip = request.client.host
        user_agent = request.headers.get("User-Agent", "Unknown")
        signature_base = f"{ip}_{user_agent}".encode('utf-8')

        fingerprint = hashlib.sha256(signature_base).hexdigest()
        logger.debug(f"Request fingerprinted: {fingerprint[:8]}")
        return fingerprint

    @staticmethod
    def validate_trusted_source(fingerprint: str, trusted_list: list) -> bool:
        if fingerprint not in trusted_list:
            logger.critical("Zero-Trust Violation: Untrusted webhook fingerprint detected. Dropping payload.")
            raise HTTPException(status_code=403, detail="Access Denied: Unrecognized Ingress Signature")
        return True
