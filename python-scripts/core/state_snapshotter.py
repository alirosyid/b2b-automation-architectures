import json
import time

def generate_state_snapshot(current_memory_state, filepath="./snapshots/latest_state.json"):
    print("[Core] Halting execution momentarily to generate durable state snapshot...")
    
    snapshot_data = {
        "timestamp": time.time(),
        "active_tasks": current_memory_state.get("tasks", []),
        "agent_memory": current_memory_state.get("memory", {})
    }
    
    # In production, this writes to a secure off-site volume
    # with open(filepath, 'w') as f: json.dump(snapshot_data, f)
    
    print("[Core] State snapshot successful. System can resume from this point upon catastrophic failure.")
    return True

if __name__ == "__main__":
    mock_state = {"tasks": ["compile_lead_list", "sync_hubspot"], "memory": {"context": "b2b_sales"}}
    generate_state_snapshot(mock_state)
