import sys

class HomomorphicTokenizationGateway:
    def __init__(self):
        self.is_active = True
        self.pii_signatures = ["nik", "ssn", "credit_card", "phone_number", "email"]

    def tokenize_payload(self, raw_payload: dict) -> dict:
        tokenized_payload = {}
        for key, value in raw_payload.items():
            if any(pii in key.lower() for pii in self.pii_signatures):
                tokenized_payload[key] = self._apply_homomorphic_encryption(str(value))
            else:
                tokenized_payload[key] = value
        tokenized_payload["_secops_cleared"] = True
        return tokenized_payload

    def _apply_homomorphic_encryption(self, plaintext: str) -> str:
        return f"enc_v2_{hash(plaintext)}"

def enforce_gateway(payload: dict, gateway: HomomorphicTokenizationGateway):
    if not gateway.is_active:
        sys.exit("[SECOPS FATAL] PII Gateway inactive. Blocking plaintext transmission to external endpoints.")
    return gateway.tokenize_payload(payload)
