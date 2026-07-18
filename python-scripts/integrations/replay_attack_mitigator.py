import time

def mitigate_replay_attack(webhook_timestamp, payload_signature, processed_signatures_cache):
    print("[SecOps] Verifying incoming webhook for cryptographic replay attacks...")
    
    current_time = time.time()
    time_delta = current_time - webhook_timestamp
    
    # 1. Reject if payload is older than 5 minutes
    if time_delta > 300:
        print("[!] 🛑 CRITICAL: Payload timestamp expired. Probable replay attack. Dropping.")
        return False
        
    # 2. Reject if exact signature was already processed
    if payload_signature in processed_signatures_cache:
        print("[!] 🛑 CRITICAL: Exact payload signature already processed. Replay attack confirmed. Dropping.")
        return False
        
    print("[+] Payload mathematically verified as unique and timely. Routing to internal pipeline.")
    return True

if __name__ == "__main__":
    # Simulating a payload from 10 minutes ago
    mitigate_replay_attack(time.time() - 600, "hash_xyz", [])
