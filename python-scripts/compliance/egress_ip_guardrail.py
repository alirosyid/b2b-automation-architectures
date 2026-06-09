import logging

class EgressDataGuardrailDemo:
    """
    PORTFOLIO SHOWCASE: LLM Output Egress Filter.
    Demonstrates blocking data exfiltration and cross-tenant hallucination leaks.
    """
    def __init__(self):
        self.restricted_patterns = ["internal_api_key", "tenant_db_url", "sys_admin"]

    def sanitize_output_dry_run(self, llm_response: str, tenant_id: str) -> str:
        logging.info(f"[PORTFOLIO MOCK] Scanning LLM egress payload for tenant {tenant_id}...")
        
        for pattern in self.restricted_patterns:
            if pattern in llm_response.lower():
                logging.critical(f"[SECOPS FATAL] Egress blocked! Detected restricted IP/Data: {pattern}")
                # In production, this raises an alert and returns a sanitized safe-string
                return "[REDACTED BY ENTERPRISE GUARDRAIL]"
                
        logging.info("[SECOPS MOCK] Egress payload clean. Transmitting to client.")
        return llm_response
