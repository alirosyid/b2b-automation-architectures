import re
from typing import Dict

class ZeroTrustPIIGateway:
    def __init__(self):
        # Strict global pattern matching for EU/US standards
        self.email_pattern = re.compile(r'[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+')
        self.phone_pattern = re.compile(r'\+?\d{10,14}')

    def sanitize_payload(self, raw_data: Dict[str, str]) -> Dict[str, str]:
        sanitized = {}
        for key, value in raw_data.items():
            safe_val = self.email_pattern.sub("[REDACTED_EMAIL]", value)
            safe_val = self.phone_pattern.sub("[REDACTED_PHONE]", safe_val)
            sanitized[key] = safe_val
        return sanitized

gateway = ZeroTrustPIIGateway()
test_payload = {"lead_name": "John Doe", "contact": "johndoe@globalcorp.com", "phone": "+14155552671"}
print(gateway.sanitize_payload(test_payload))
