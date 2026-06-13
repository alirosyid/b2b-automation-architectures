import logging

class ChurnPredictionInterceptor:
    def __init__(self):
        self.critical_keywords = ["cancel", "unacceptable", "competitor", "refund", "downtime"]

    def evaluate_payload_dry_run(self, ticket_payload: dict) -> str:
        logging.info(f"[PORTFOLIO MOCK] Intercepting webhook for Client: {ticket_payload.get('client_id')}")
        
        body_text = ticket_payload.get("message_body", "").lower()
        risk_flags = sum(1 for word in self.critical_keywords if word in body_text)
        
        if risk_flags >= 2:
            logging.critical(f"[BUSINESS MOCK] High Churn Risk detected ({risk_flags} flags).")
            logging.info("[BUSINESS MOCK] Overriding default router. Escalating to Tier 1 Retention Queue.")
            return "ROUTE_TO_RETENTION_TEAM"
            
        logging.info("[BUSINESS MOCK] Payload sentiment nominal. Routing to standard L1 support.")
        return "ROUTE_TO_STANDARD"
