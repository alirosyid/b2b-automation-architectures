import logging

class HomomorphicTokenizationGatewayDemo:
    """
    PORTFOLIO SHOWCASE: PII Interception Gateway.
    Demonstrates mandatory tokenization before LLM dispatch.
    """
    def __init__(self, is_active: bool = True):
        self.is_active = is_active
        self.pii_signatures = ["nik", "ssn", "credit_card", "phone_number"]

    def tokenize_payload_dry_run(self, raw_payload: dict) -> dict:
        if not self.is_active:
             logging.critical("[SECOPS FATAL DEMO] Gateway bypass attempted. Halting execution instantly.")
             return {"error": "halted_by_secops"}

        tokenized_payload = {}
        for key, value in raw_payload.items():
            if any(pii in key.lower() for pii in self.pii_signatures):
                tokenized_payload[key] = f"[PORTFOLIO_ENCRYPTED_MOCK]_{hash(str(value))}"
            else:
                tokenized_payload[key] = value
                
        tokenized_payload["_secops_cleared"] = True
        return tokenized_payload
