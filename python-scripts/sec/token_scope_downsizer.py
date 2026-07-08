def analyze_and_restrict_scopes(api_key_id, access_logs, current_scopes):
    print(f"[SecOps] Auditing permission scopes for token: {api_key_id}")
    
    used_scopes = set([log["action_type"] for log in access_logs])
    unused_scopes = set(current_scopes) - used_scopes
    
    if unused_scopes:
        print(f"[!] Token is over-privileged. Unused scopes detected: {unused_scopes}")
        print("    -> Initiating autonomous scope down-sizing to enforce Zero-Trust.")
        # Mocking API call to Identity Provider to restrict key
        optimized_scopes = list(used_scopes)
        print(f"[+] Token secured. New restrictive scopes: {optimized_scopes}")
        return optimized_scopes
        
    print("[+] Token scoping is perfectly optimized.")
    return current_scopes

if __name__ == "__main__":
    logs = [{"action_type": "read:leads"}, {"action_type": "read:leads"}]
    current = ["read:leads", "write:leads", "delete:leads"]
    analyze_and_restrict_scopes("key_prod_8842", logs, current)
