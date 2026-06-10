import logging

class ContextKnapsackOptimizer:
    """
    PORTFOLIO SHOWCASE: FinOps Context Optimization.
    Maximizes RAG relevance while strictly adhering to a token cost budget.
    """
    def __init__(self, max_token_budget: int):
        self.max_budget = max_token_budget

    def optimize_context_dry_run(self, retrieved_chunks: list[dict]) -> list[dict]:
        logging.info(f"[PORTFOLIO MOCK] Running Knapsack algorithm for token budget: {self.max_budget}")
        
        # Sort by highest relevance score first (Greedy Knapsack approach)
        retrieved_chunks.sort(key=lambda x: x.get("relevance_score", 0), reverse=True)
        
        optimized_context = []
        current_tokens = 0
        
        for chunk in retrieved_chunks:
            chunk_tokens = chunk.get("token_count", 0)
            if current_tokens + chunk_tokens <= self.max_budget:
                optimized_context.append(chunk)
                current_tokens += chunk_tokens
            else:
                logging.info(f"[FINOPS MOCK] Chunk excluded to prevent budget breach. Saved {chunk_tokens} tokens.")
                
        logging.info(f"[FINOPS MOCK] Context optimized. Total tokens used: {current_tokens}/{self.max_budget}")
        return optimized_context
