import random
import json

class SyntheticLeadGenerator:
    """
    Generates structurally valid but entirely fictitious B2B lead data.
    Enables high-volume pipeline load testing without violating data privacy laws.
    """
    COMPANIES = ["Acme Corp", "Globex", "Initech", "Soylent"]
    TITLES = ["CEO", "CTO", "VP of Engineering", "Director of Sales"]

    @classmethod
    def generate_batch(cls, count: int = 100) -> str:
        leads = []
        for i in range(count):
            leads.append({
                "id": f"lead_{i}",
                "company": random.choice(cls.COMPANIES),
                "job_title": random.choice(cls.TITLES),
                "email": f"test_{i}@example.com",
                "annual_revenue": random.randint(1000000, 50000000)
            })
        return json.dumps(leads)
