import requests

def enrich_lead_with_perplexity(company_name, api_key):
    print(f"[Lead Gen] Querying Perplexity Sonnet for real-time intel on: {company_name}")
    
    url = "https://api.perplexity.ai/chat/completions"
    payload = {
        "model": "llama-3-sonar-large-32k-online",
        "messages": [
            {"role": "system", "content": "Return a JSON summary of the company's tech stack, recent news, and estimated revenue."},
            {"role": "user", "content": f"Analyze {company_name}."}
        ]
    }
    headers = {"Authorization": f"Bearer {api_key}", "Content-Type": "application/json"}
    
    # Mocking response
    # response = requests.post(url, json=payload, headers=headers)
    enriched_data = {
        "company": company_name,
        "recent_news": "Just launched a new AI workflow suite.",
        "tech_stack": ["AWS", "Node.js", "GraphQL"]
    }
    
    print(f"[+] Enrichment complete. Routing to B2B outbound sequence.")
    return enriched_data

if __name__ == "__main__":
    enrich_lead_with_perplexity("TechCorp Enterprise", "sk-mock-key")
