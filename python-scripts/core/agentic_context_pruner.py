def prune_context_window(agent_history, max_tokens=4000):
    print(f"[Core] Analyzing agent memory footprint. Current length: {len(agent_history)} messages.")
    
    optimized_history = []
    retained_tokens = 0
    
    # Keep system prompt and most recent messages, compress the middle
    for msg in reversed(agent_history):
        msg_tokens = len(msg["content"].split()) # Mock token count
        
        if retained_tokens + msg_tokens < max_tokens or msg["role"] == "system":
            optimized_history.insert(0, msg)
            retained_tokens += msg_tokens
        else:
            print(f"    🗑️ Pruning low-relevance memory block to prevent token bloat.")
            
    print(f"[+] Context window optimized. Token reduction: {len(agent_history) - len(optimized_history)} messages dropped.")
    return optimized_history

if __name__ == "__main__":
    history = [{"role": "system", "content": "You are a B2B AI."}] + [{"role": "user", "content": "noise"} for _ in range(50)]
    prune_context_window(history)
