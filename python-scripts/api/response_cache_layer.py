import hashlib

class APICacheLayer:
    def __init__(self):
        self.redis_mock_db = {} # Simulating Redis in-memory storage

    def fetch_response(self, request_payload, query_function):
        payload_hash = hashlib.md5(str(request_payload).encode()).hexdigest()
        
        if payload_hash in self.redis_mock_db:
            print("[API Gateway] ⚡ Cache HIT. Serving request with zero latency.")
            return self.redis_mock_db[payload_hash]
            
        print("[API Gateway] 🐢 Cache MISS. Executing heavy database/LLM query.")
        response = query_function(request_payload)
        self.redis_mock_db[payload_hash] = response
        return response

def mock_heavy_query(payload):
    return {"status": "success", "data": "Processed Result"}

if __name__ == "__main__":
    cache = APICacheLayer()
    cache.fetch_response({"query": "get_active_leads"}, mock_heavy_query)
    cache.fetch_response({"query": "get_active_leads"}, mock_heavy_query) # Hits cache
