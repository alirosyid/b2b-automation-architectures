import numpy as np

class SemanticCacheMiddleware:
    def __init__(self, vector_store, similarity_threshold=0.96):
        self.vector_store = vector_store
        self.similarity_threshold = similarity_threshold

    def fetch_or_compute(self, user_prompt, embedding_function, llm_function):
        print("[API Ops] Checking Redis Vector Store for semantic cache hit...")
        prompt_embedding = embedding_function(user_prompt)
        
        # Search for semantically similar previous queries
        nearest_neighbor = self.vector_store.search(prompt_embedding, top_k=1)
        
        if nearest_neighbor and nearest_neighbor['score'] >= self.similarity_threshold:
            print(f"[+] ⚡ CACHE HIT (Similarity: {nearest_neighbor['score']:.3f}). Returning cached response in 4ms.")
            return nearest_neighbor['cached_response']
            
        print("[-] Cache Miss. Routing to premium LLM endpoint...")
        response = llm_function(user_prompt)
        
        # Asynchronously store new embedding and response for future hits
        self.vector_store.upsert(prompt_embedding, response)
        return response

if __name__ == "__main__":
    cache = SemanticCacheMiddleware(vector_store="redis_mock")
    # cache.fetch_or_compute("How do I integrate n8n with HubSpot?", mock_embed, mock_llm)
