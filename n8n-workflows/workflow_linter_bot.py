import json

def lint_n8n_workflow(workflow_json):
    print("[N8N Ops] Scanning workflow architecture for anti-patterns and security risks...")
    issues_found = []
    
    for node in workflow_json.get("nodes", []):
        # Check for hardcoded credentials
        if "api_key" in str(node.get("parameters", {})).lower():
            issues_found.append(f"Hardcoded credential risk in node: {node['name']}")
            
        # Check for HTTP requests without timeout constraints
        if node["type"] == "n8n-nodes-base.httpRequest" and "timeout" not in node.get("parameters", {}):
            issues_found.append(f"Missing timeout constraint in HTTP node: {node['name']}")
            
    if issues_found:
        print(f"[!] 🚨 Linter failed. Found {len(issues_found)} critical issues.")
        for issue in issues_found: print(f"    - {issue}")
        return False
        
    print("[+] Workflow passed all security and architecture checks.")
    return True

if __name__ == "__main__":
    mock_workflow = {"nodes": [{"name": "Fetch API", "type": "n8n-nodes-base.httpRequest", "parameters": {"api_key": "12345"}}]}
    lint_n8n_workflow(mock_workflow)
