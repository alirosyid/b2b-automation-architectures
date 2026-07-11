def allocate_token_costs(client_usage_logs, cost_per_1k_tokens=0.01):
    print("[FinOps] Aggregating distributed LLM token usage per B2B client...")
    billing_payloads = []
    
    for client, tokens in client_usage_logs.items():
        total_cost = (tokens / 1000) * cost_per_1k_tokens
        print(f"[+] {client}: {tokens} tokens consumed. Cost: ${total_cost:.2f}")
        billing_payloads.append({"client": client, "stripe_charge": total_cost})
        
    print("[+] Pushing usage-based billing data directly to Stripe API.")
    return billing_payloads

if __name__ == "__main__":
    logs = {"Enterprise_A": 450000, "Startup_B": 12500}
    allocate_token_costs(logs)
