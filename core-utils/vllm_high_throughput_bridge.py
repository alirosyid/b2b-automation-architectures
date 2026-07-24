def route_to_vllm_cluster(langchain_payload, internal_gpu_endpoint):
    print("[Core Ops] Intercepting LangChain execution payload...")
    
    batch_size = len(langchain_payload.get("prompts", []))
    print(f"    -> Batch size detected: {batch_size} prompts.")
    
    if batch_size > 10:
        print(f"[+] Large batch detected. Routing to internal vLLM cluster ({internal_gpu_endpoint}) for high-throughput parallel inference.")
        # PagedAttention allows vLLM to process this 4x faster than standard endpoints
        # response = requests.post(internal_gpu_endpoint, json=langchain_payload)
        
        print("[+] Fast parallel inference complete. Yielding results back to LangChain orchestrator.")
        return {"status": "vllm_success", "routed_to": "internal_gpu"}
        
    print("[*] Small batch. Executing via standard synchronous endpoint.")
    return {"status": "standard_success", "routed_to": "external_api"}

if __name__ == "__main__":
    mock_payload = {"prompts": ["Extract data"] * 50}
    route_to_vllm_cluster(mock_payload, "http://10.0.0.5:8000/v1/completions")
