import random
import json

def generate_synthetic_lead():
    industries = ["FinTech", "HealthTech", "Logistics", "SaaS"]
    roles = ["CEO", "VP of Ops", "Director of IT", "Founder"]
    
    lead = {
        "company_name": f"MockCorp {random.randint(100, 999)}",
        "industry": random.choice(industries),
        "decision_maker": f"Test {random.choice(roles)}",
        "annual_revenue": random.choice([500000, 1500000, 5000000, 10000000]),
        "pain_point": "Manual API routing causing 504 timeouts"
    }
    return lead

def batch_generate(count=100):
    print(f"[Data] Generating {count} synthetic B2B leads for local pipeline testing...")
    dataset = [generate_synthetic_lead() for _ in range(count)]
    
    with open("synthetic_leads.json", "w") as f:
        json.dump(dataset, f, indent=2)
        
    print("[Data] Synthetic dataset created. 100% PII-free and safe for testing.")
    return dataset

if __name__ == "__main__":
    batch_generate(50)
