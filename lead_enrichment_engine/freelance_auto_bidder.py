def evaluate_and_bid(job_description, budget):
    target_keywords = ["api integration", "n8n", "process automation", "b2b"]
    
    if budget < 1000:
        return "[Enrichment] Ignored: Budget too low for enterprise SLA."
        
    if any(kw in job_description.lower() for kw in target_keywords):
        print(f"[Enrichment] High-Ticket Match Found! Budget: ${budget}. Generating proposal...")
        proposal = "Hi, we specialize in high-availability backend automations. We can architect this solution using edge-hosted APIs to guarantee 99.9% uptime."
        # API logic to submit proposal
        return proposal
        
    return "[Enrichment] Ignored: Job scope does not match core competencies."

if __name__ == "__main__":
    desc = "Need someone to build a complex n8n workflow to route our B2B leads."
    print(evaluate_and_bid(desc, 2500))
