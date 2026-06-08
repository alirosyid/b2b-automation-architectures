import sys

class MarginAwareTokenGovernor:
    def __init__(self, token_budget_limit: float):
        self.budget_limit = token_budget_limit
        self.current_spend = 0.0
        self.homomorphic_gateway_active = True 

    def analyze_complexity(self, payload: dict) -> float:
        return len(str(payload)) * 0.0015 

    def execute_arbitrage_routing(self, payload: dict, core_business_extraction_func):
        if not self.homomorphic_gateway_active:
            raise PermissionError("[SECOPS HALT] Homomorphic Gateway bypassed. Execution terminated.")
            
        estimated_cost = self.analyze_complexity(payload)
        
        if (self.current_spend + estimated_cost) > self.budget_limit:
            sys.exit(f"[FINOPS HALT] Estimated token cost ({estimated_cost}) exceeds ROI margin tolerance. Halting.")
            
        self.current_spend += estimated_cost
        extracted_data = core_business_extraction_func(payload)
        
        if estimated_cost < 2.5:
            return self._route_to_local_model(extracted_data)
        return self._route_to_premium_llm(extracted_data)

    def _route_to_local_model(self, data): return data
    def _route_to_premium_llm(self, data): return data
