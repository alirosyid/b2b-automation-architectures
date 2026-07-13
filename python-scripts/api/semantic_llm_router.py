import numpy as np

class SemanticRouter:
    def __init__(self, vector_db):
        self.db = vector_db
        # Pre-calculated centroid vectors for complex logic vs simple extraction
        self.complex_centroid = np.array([0.15, -0.82, 0.44]) 
        self.simple_centroid = np.array([-0.05, 0.22, -0.11])

    def route_prompt(self, user_prompt, embedding_function):
        print(f"[API Gateway] Analyzing semantic complexity of inbound prompt...")
        prompt_vector = embedding_function(user_prompt)
        
        # Calculate cosine similarity
        complex_dist = np.dot(prompt_vector, self.complex_centroid)
        simple_dist = np.dot(prompt_vector, self.simple_centroid)
        
        if complex_dist > simple_dist:
            print("[+] High complexity detected. Routing to Premium Engine (GPT-4o).")
            return "premium_engine"
            
        print("[+] Low complexity detected. Routing to Edge Engine (Llama-3) to maximize margin.")
        return "edge_engine"

if __name__ == "__main__":
    router = SemanticRouter("mock_db")
    router.route_prompt("Map this JSON to the HubSpot schema.", lambda x: np.array([0.1, -0.8, 0.4]))
