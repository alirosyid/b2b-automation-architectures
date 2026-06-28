class RAGCostAnalyzer:
    def __init__(self, cost_per_1k_tokens=0.002):
        self.cost_rate = cost_per_1k_tokens
        self.client_budgets = {"ENT-001": 5.00, "ENT-002": 15.00} # Daily budget limits in USD

    def evaluate_query_cost(self, client_id, estimated_tokens, current_daily_spend):
        query_cost = (estimated_tokens / 1000) * self.cost_rate
        projected_spend = current_daily_spend + query_cost
        
        budget_limit = self.client_budgets.get(client_id, 1.00)
        
        if projected_spend > budget_limit:
            print(f"[FinOps] 🛑 Query BLOCKED for {client_id}. Projected spend (${projected_spend:.4f}) exceeds daily cap (${budget_limit:.2f}).")
            return {"status": "blocked", "reason": "budget_exceeded"}
            
        print(f"[FinOps] ✅ Query approved. Estimated cost: ${query_cost:.4f}")
        return {"status": "approved", "projected_spend": projected_spend}

if __name__ == "__main__":
    analyzer = RAGCostAnalyzer()
    analyzer.evaluate_query_cost("ENT-001", estimated_tokens=150000, current_daily_spend=4.85)
