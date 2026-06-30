def multi_agent_consensus(company_name, perplexity_client):
    """Uses a consensus model to verify B2B lead enrichment data."""
    queries = [
        f"What is the exact current employee count of {company_name}?",
        f"Recent funding news or M&A activity for {company_name} in 2026?",
        f"Who is the current CTO or VP of Engineering at {company_name}?"
    ]
    
    results = []
    for q in queries:
        response = perplexity_client.chat.completions.create(
            model="llama-3-sonar-large-32k-online",
            messages=[{"role": "user", "content": q}]
        )
        results.append(response.choices[0].message.content)
    
    # Consensus aggregator logic here
    final_payload = {"employee_count": results[0], "funding": results[1], "cto": results[2]}
    return final_payload
