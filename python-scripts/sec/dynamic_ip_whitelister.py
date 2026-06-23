def sync_firewall_whitelist(active_client_ips):
    print("[SecOps] Fetching approved IP ranges from CRM database...")
    
    current_firewall_rules = ["192.168.1.1", "10.0.0.5"] # Mock existing
    updated_rules = list(set(current_firewall_rules + active_client_ips))
    
    print(f"[SecOps] 🛡️ Applying dynamic whitelist to API Gateway. Total allowed IPs: {len(updated_rules)}")
    # Code to push rules to AWS WAF or Nginx config goes here
    
    return updated_rules

if __name__ == "__main__":
    new_client_ips = ["203.0.113.45", "198.51.100.12"]
    sync_firewall_whitelist(new_client_ips)
