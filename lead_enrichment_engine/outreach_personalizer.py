import json

def generate_personalized_intro(company_name, recent_news):
    # Simulates sending context to an LLM to generate an icebreaker
    prompt = f"Write a casual, 1-sentence B2B cold email intro for {company_name} referencing this news: {recent_news}"
    
    # Mock LLM Response
    icebreaker = f"Saw your recent expansion into the European market with {company_name}—huge milestone, congrats!"
    
    return {
        "company": company_name,
        "personalized_intro": icebreaker,
        "status": "ready_for_dispatch"
    }

if __name__ == "__main__":
    lead = generate_personalized_intro("TechFlow", "Launched a new predictive AI suite")
    print(json.dumps(lead, indent=2))
