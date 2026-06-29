def scan_and_revoke_leaks(active_keys, threat_intel_feed):
    print("[SecOps] Cross-referencing active API keys against global threat intel feeds...")
    
    compromised = False
    for key_id, key_value in active_keys.items():
        if key_value in threat_intel_feed:
            print(f"[!] CRITICAL LEAK DETECTED: {key_id} found in public gist.")
            _revoke_key(key_id)
            compromised = True
            
    if not compromised:
        print("[+] All API keys secure. No public leaks detected.")

def _revoke_key(key_id):
    print(f"    -> Executing automated revocation protocol for {key_id} via provider API.")

if __name__ == "__main__":
    mock_keys = {"client_a_openai": "sk-12345", "client_b_stripe": "sk_live_98765"}
    mock_feed = ["sk-99999", "sk-12345"] # client_a_openai is leaked
    scan_and_revoke_leaks(mock_keys, mock_feed)
