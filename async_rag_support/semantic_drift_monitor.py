import random

class DriftMonitor:
    def __init__(self, confidence_threshold=0.85):
        self.confidence_threshold = confidence_threshold

    def evaluate_query_relevance(self, user_query, retrieved_vector_score):
        # retrieved_vector_score simulates cosine similarity
        if retrieved_vector_score < self.confidence_threshold:
            print(f"[RAG] ⚠️ Semantic Drift Detected! Score {retrieved_vector_score} is below threshold.")
            return {"action": "flag_for_refresh", "query": user_query}
            
        return {"action": "stable", "query": user_query}

if __name__ == "__main__":
    monitor = DriftMonitor()
    # Simulating a query about a newly released product not fully in the DB
    print(monitor.evaluate_query_relevance("How does the new 2026 Quantum Router work?", 0.65))
