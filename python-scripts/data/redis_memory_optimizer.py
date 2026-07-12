import json

class AgentMemoryOptimizer:
    def __init__(self):
        # Mocking Redis in-memory store
        self.redis_store = {}

    def fetch_or_initialize_context(self, session_id):
        print(f"[Data] Retrieving low-latency agent memory for session: {session_id}")
        
        if session_id in self.redis_store:
            context = self.redis_store[session_id]
            print(f"[+] Memory HIT. Injecting {len(context)} bytes of context into prompt.")
            return context
            
        print("[-] Memory MISS. Initializing blank contextual state.")
        self.redis_store[session_id] = []
        return []

    def append_memory(self, session_id, new_interaction):
        current_memory = self.fetch_or_initialize_context(session_id)
        current_memory.append(new_interaction)
        
        # Enforce sliding window to prevent token bloat
        if len(current_memory) > 10:
            current_memory.pop(0)
            
        self.redis_store[session_id] = current_memory
        print(f"[+] Interaction compressed and stored. Context window optimized.")

if __name__ == "__main__":
    memory_db = AgentMemoryOptimizer()
    memory_db.append_memory("client_chat_992", {"role": "user", "content": "I need API routing."})
