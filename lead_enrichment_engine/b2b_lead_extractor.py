import os
import requests
import json
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from dotenv import load_dotenv

load_dotenv()

app = FastAPI()

class Payload(BaseModel):
    company_data: str

class LeadArchitect:
    def __init__(self):
        self.groq_key = os.getenv("GROQ_API_KEY")
        # Clean URL, no formatting artifacts
        self.base_url = "https://api.groq.com/openai/v1/chat/completions"

    def enrich_data(self, company_data):
        if not self.groq_key:
            return {"error": "GROQ_API_KEY not found in .env file!"}
            
        headers = {
            "Authorization": f"Bearer {self.groq_key}",
            "Content-Type": "application/json"
        }
        
        # 6-COMPONENT PROMPT TO ENFORCE PURE JSON OUTPUT
        prompt = f"""
        [ROLE] Senior B2B Business Analyst & AI Architect.
        [TASK] Extract exactly 3 critical technical/business bottlenecks based on the provided company data.
        [INPUT] {company_data}
        [OUTPUT] You MUST output ONLY a valid JSON object. 
        [CONSTRAINTS] DO NOT output any conversational text. DO NOT use markdown tags like ```json. The response must start with {{ and end with }}.
        [CAPABILITIES] Deep analytical reasoning to find hidden pain points.
        
        SCHEMA REQUIRED:
        {{
            "company": "Name of Company",
            "business_category": "Industry",
            "bottlenecks": [
                {{"issue": "...", "business_impact": "..."}}
            ]
        }}
        """
        
        payload = {
            "model": "llama-3.3-70b-versatile",
            "messages": [{"role": "user", "content": prompt}],
            "response_format": {"type": "json_object"}, # Key to ensuring pure JSON output
            "temperature": 0.1
        }
        
        response = requests.post(self.base_url, json=payload, headers=headers)
        
        # GROQ ERROR TRACKER
        if response.status_code != 200:
            print("===========================")
            print("GROQ REJECTED YOUR REQUEST!")
            print(f"Status Code: {response.status_code}")
            print(f"Reason: {response.text}")
            print("===========================")
            return {"error": response.text}
            
        raw_content = response.json()['choices'][0]['message']['content']
        
        # JSON PARSING
        try:
            clean_json = json.loads(raw_content)
            return clean_json
        except Exception as e:
            return {"error": f"Failed to parse JSON from AI. Error: {str(e)}"}

@app.post("/enrich")
async def enrich_endpoint(payload: Payload):
    architect = LeadArchitect()
    result = architect.enrich_data(payload.company_data)
    
    if "error" in result:
        raise HTTPException(status_code=400, detail=result["error"])
        
    return {"status": "success", "ai_analysis": result}
