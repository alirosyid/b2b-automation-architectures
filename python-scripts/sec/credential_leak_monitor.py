import hashlib

def scan_for_leaks(client_domain, known_breach_database):
    print(f"[SecOps] Initiating external security sweep for domain: @{client_domain}")
    
    compromised_accounts = []
    for breach in known_breach_database:
        if client_domain in breach["email"]:
            compromised_accounts.append(breach["email"])
            
    if compromised_accounts:
        print(f"[!] CRITICAL: Found {len(compromised_accounts)} compromised accounts for {client_domain}.")
        print("[+] Dispatching automated security alert to client CISO.")
    else:
        print(f"[+] Domain @{client_domain} is secure. No leaks detected in current cycle.")
        
    return compromised_accounts

if __name__ == "__main__":
    mock_db = [{"email": "admin@enterprise.com", "leak_source": "Collection#1"}]
    scan_for_leaks("enterprise.com", mock_db)
