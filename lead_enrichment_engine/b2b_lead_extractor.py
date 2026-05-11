import os
import requests
from dotenv import load_dotenv

load_dotenv()

class LeadArchitect:
    def __init__(self):
        self.groq_key = os.getenv("GROQ_API_KEY")
        self.base_url = "https://api.groq.com/openai/v1/chat/completions"

    def enrich_data(self, company_data):
        """Menggunakan AI untuk menganalisis bottleneck perusahaan"""
        headers = {
            "Authorization": f"Bearer {self.groq_key}",
            "Content-Type": "application/json"
        }
        
        prompt = f"Analyze this company data and identify 3 potential automation bottlenecks: {company_data}"
        
        payload = {
            "model": "llama3-70b-8192",
            "messages": [{"role": "user", "content": prompt}]
        }
        
        response = requests.post(self.base_url, json=payload, headers=headers)
        return response.json()['choices'][0]['message']['content']

# Kode ini siap diintegrasikan dengan n8n atau dijalankan standalone
if __name__ == "__main__":
    architect = LeadArchitect()
    # Contoh data mentah dari scraper
    sample_data = "TechFlow Inc, B2B SaaS, manual lead scoring process"
    print(architect.enrich_data(sample_data))