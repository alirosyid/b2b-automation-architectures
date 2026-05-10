import hmac
import hashlib
from fastapi import HTTPException, Security
from fastapi.security import APIKeyHeader

header_scheme = APIKeyHeader(name="X-B2B-Signature")

class ZeroTrustValidator:
    """
    Enforces Zero-Trust architecture on all incoming automation triggers.
    Rejects any payload lacking a valid cryptographic signature.
    """
    @staticmethod
    def verify_payload(payload_body: bytes, secret_key: str, signature: str = Security(header_scheme)):
        expected_hmac = hmac.new(
            key=secret_key.encode(),
            msg=payload_body,
            digestmod=hashlib.sha256
        ).hexdigest()

        if not hmac.compare_digest(expected_hmac, signature):
            raise HTTPException(status_code=403, detail="Zero-Trust Policy Violation: Invalid Signature")
        return True
