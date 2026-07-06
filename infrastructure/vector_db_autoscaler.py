def monitor_vector_db_latency(current_latency_ms, active_replicas):
    target_latency = 50.0
    max_replicas = 5
    
    print(f"[Infra] Current Vector Search Latency: {current_latency_ms}ms")
    
    if current_latency_ms > target_latency:
        if active_replicas < max_replicas:
            new_replicas = active_replicas + 1
            print(f"[Infra] 📈 Latency degrading. Scaling Vector DB read-replicas to {new_replicas}...")
            # Trigger K8s scaling command
            return new_replicas
        else:
            print("[Infra] ⚠️ Max database replicas reached. Scaling blocked.")
            return active_replicas
            
    print("[+] Database latency within optimal performance envelope.")
    return active_replicas

if __name__ == "__main__":
    monitor_vector_db_latency(current_latency_ms=65.4, active_replicas=2)
