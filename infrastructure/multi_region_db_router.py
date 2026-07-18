def route_query_by_region(client_ip_region, query_payload):
    print(f"[Infra] Intercepting DB query from region: {client_ip_region}")
    
    # Global Replica Map
    replica_map = {
        "EU": "eu-west-1.db.internal",
        "US": "us-east-1.db.internal",
        "ASIA": "ap-southeast-1.db.internal"
    }
    
    target_node = replica_map.get(client_ip_region, replica_map["US"])
    
    print(f"[+] Optimal routing calculated. Dispatching query to {target_node} to guarantee sub-10ms latency.")
    # Mocking Database execution
    
    return {"status": "routed", "node": target_node}

if __name__ == "__main__":
    route_query_by_region("EU", {"action": "INSERT", "data": "lead_1042"})
