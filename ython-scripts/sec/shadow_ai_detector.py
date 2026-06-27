def scan_network_for_shadow_ai(network_logs):
    print("[SecOps] Scanning outbound traffic for unauthorized LLM endpoints...")
    
    unauthorized_endpoints = ["api.anthropic.com", "api.openai.com", "api.cohere.ai"]
    violations = []
    
    for log in network_logs:
        if any(endpoint in log["destination"] for endpoint in unauthorized_endpoints):
            if not log.get("is_via_gateway", False):
                violations.append(log)
                
    if violations:
        print(f"[!] SECURITY BREACH: {len(violations)} instances of Shadow AI usage detected bypassing the central gateway.")
        # Trigger internal security alert
    else:
        print("[+] Network secure. All AI traffic routed through authorized Zero-Trust gateways.")
        
    return violations

if __name__ == "__main__":
    mock_logs = [
        {"user": "dev_1", "destination": "api.openai.com", "is_via_gateway": True},
        {"user": "contractor_2", "destination": "api.anthropic.com", "is_via_gateway": False} # Violation
    ]
    scan_network_for_shadow_ai(mock_logs)
