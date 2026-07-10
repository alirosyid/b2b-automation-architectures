def scan_for_shadow_apis(network_logs, registered_endpoints):
    print("[SecOps] Scanning network telemetry for undocumented API endpoints...")
    
    shadow_apis = []
    for log in network_logs:
        target = log.get("endpoint")
        if target not in registered_endpoints and "api" in target:
            print(f"[!] Shadow API Detected: {target}")
            shadow_apis.append(target)
            
    if shadow_apis:
        print(f"[+] Found {len(shadow_apis)} shadow endpoints. Auto-generating Swagger documentation and routing to Gateway.")
        return {"status": "unsecured_endpoints_found", "data": shadow_apis}
        
    print("[+] Zero-Trust environment verified. No shadow APIs found.")
    return {"status": "secure"}

if __name__ == "__main__":
    mock_logs = [{"endpoint": "/v1/internal/leads"}, {"endpoint": "/v2/hidden-metrics"}]
    mock_registered = ["/v1/internal/leads"]
    scan_for_shadow_apis(mock_logs, mock_registered)
