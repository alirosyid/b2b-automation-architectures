class MultiTenantCostAllocator:
    """
    Melacak dan mengatribusikan biaya token LLM ke masing-masing ID Klien.
    Penting untuk model penagihan B2B (Chargeback/Invoicing).
    """
    def __init__(self):
        self.client_usage_db = {} # Simulasi DB

    def log_client_cost(self, client_id: str, cost_usd: float):
        if client_id not in self.client_usage_db:
            self.client_usage_db[client_id] = 0.0
        self.client_usage_db[client_id] += cost_usd

    def generate_invoice_data(self, client_id: str, markup_percentage: float = 20.0) -> dict:
        base_cost = self.client_usage_db.get(client_id, 0.0)
        final_billing = base_cost * (1 + (markup_percentage / 100))
        return {"client_id": client_id, "api_cost": base_cost, "amount_due": final_billing}
