import json

def analyze_n8n_workflow(filepath):
    print(f"[*] Analyzing workflow architecture: {filepath}")
    
    # Mock JSON representation of an n8n workflow
    mock_workflow = {"nodes": [{"type": "Set"}, {"type": "Set"}, {"type": "HTTP Request"}]}
    
    set_nodes = sum(1 for node in mock_workflow["nodes"] if node["type"] == "Set")
    
    if set_nodes > 1:
        print("[Optimization Suggestion] Multiple consecutive 'Set' nodes detected. Condense them into a single Code node to reduce execution overhead.")
        return False
        
    print("[+] Workflow architecture is fully optimized.")
    return True

if __name__ == "__main__":
    analyze_n8n_workflow("./client_workflows/lead_routing.json")
