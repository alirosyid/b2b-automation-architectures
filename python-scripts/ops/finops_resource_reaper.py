def reap_orphaned_resources():
    print("[FinOps] Scanning cloud infrastructure for orphaned billing leaks...")
    
    # Mocking AWS API resource discovery
    orphaned_volumes = ["vol-0a1b2c3d4e5f", "vol-9z8y7x6w5v4u"]
    unattached_ips = ["198.51.100.24"]
    
    savings = 0
    for vol in orphaned_volumes:
        print(f"    🗑️ Terminating unattached EBS volume: {vol}")
        savings += 15.00 # Estimated monthly savings per volume
        
    for ip in unattached_ips:
        print(f"    🗑️ Releasing unattached Elastic IP: {ip}")
        savings += 3.50
        
    print(f"[+] FinOps Reaper execution complete. Monthly savings recovered: ${savings:.2f}")
    return savings

if __name__ == "__main__":
    reap_orphaned_resources()
