def intelligent_arbitrage_router(prompt_text):
    complexity_markers = ["analyze", "synthesize", "code", "architecture"]
    
    is_complex = any(marker in prompt_text.lower() for marker in complexity_markers)
    
    if is_complex:
        selected_model = "gpt-4o"
        cost_est = "$0.015"
        print(f"[FinOps v2] High complexity detected. Routing to Premium Model ({selected_model}).")
    else:
        selected_model = "llama-3-70b"
        cost_est = "$0.001"
        print(f"[FinOps v2] Low complexity task. Routing to Open-Source Model ({selected_model}) to maximize margins.")
        
    return {"model": selected_model, "estimated_cost": cost_est}

if __name__ == "__main__":
    intelligent_arbitrage_router("Synthesize a multi-region K8s architecture.")
    intelligent_arbitrage_router("Format this email address.")
