import re
from typing import Dict, Any

class ZeroTrustPIIGateway:
    PII_PATTERNS = {
        "email": r"[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+",
        "phone": r"\b\d{3}[-.]?\d{3}[-.]?\d{4}\b",
        "ssn_or_id": r"\b\d{3}-\d{2}-\d{4}\b"
    }

    @staticmethod
    def _redact_string(text: str) -> str:
        for pii_type, pattern in ZeroTrustPIIGateway.PII_PATTERNS.items():
            text = re.sub(pattern, f"[REDACTED_{pii_type.upper()}]", text)
        return text

    @classmethod
    def sanitize_payload(cls, payload: Dict[str, Any]) -> Dict[str, Any]:
        """SecOps Audit: High Risk Mitigation. Blocks PII leakage to external LLMs."""
        sanitized = {}
        for key, value in payload.items():
            if isinstance(value, str):
                sanitized[key] = cls._redact_string(value)
            elif isinstance(value, dict):
                sanitized[key] = cls.sanitize_payload(value)
            elif isinstance(value, list):
                sanitized[key] = [
                    cls._redact_string(v) if isinstance(v, str) else v 
                    for v in value
                ]
            else:
                sanitized[key] = value
        return sanitized

# strict block if bypass attempted
def enforce_gateway(payload: dict):
    if payload.get("_bypass_security"):
        raise PermissionError("SecOps Alert: Attempted bypass of Homomorphic Gateway.")
    return ZeroTrustPIIGateway.sanitize_payload(payload)
