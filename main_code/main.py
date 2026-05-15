import os
import requests
import json
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from dotenv import load_dotenv

# Inisialisasi Environment & Aplikasi Utama (Hanya perlu dipanggil sekali)
load_dotenv()
app = FastAPI(title="Ali Rosyid - B2B AI Gateway")

# =====================================================================
# LOKET 1: THE LEAD ENRICHMENT (Digunakan oleh Scraper untuk menilai target)
# Target URL di n8n: http://localhost:8000/enrich
# =====================================================================

class Payload(BaseModel):
    company_data: str

class LeadArchitect:
    def __init__(self):
        self.groq_key = os.getenv("GROQ_API_KEY")
        self.base_url = "https://api.groq.com/openai/v1/chat/completions"

    def enrich_data(self, company_data):
        if not self.groq_key:
            return {"error": "GROQ_API_KEY not found in .env file!"}
            
        headers = {
            "Authorization": f"Bearer {self.groq_key}",
            "Content-Type": "application/json"
        }
        
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
            "response_format": {"type": "json_object"}, 
            "temperature": 0.1
        }
        
        response = requests.post(self.base_url, json=payload, headers=headers)
        
        if response.status_code != 200:
            print("===========================")
            print("GROQ REJECTED YOUR REQUEST!")
            print(f"Status Code: {response.status_code}")
            print(f"Reason: {response.text}")
            print("===========================")
            return {"error": response.text}
            
        raw_content = response.json()['choices'][0]['message']['content']
        
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


# =====================================================================
# LOKET 2: THE RAG BOT (Digunakan untuk membalas email klien otomatis)
# Target URL di n8n: http://localhost:8000/generate_reply
# =====================================================================

class IncomingEmail(BaseModel):
    sender_email: str
    email_body: str

class RAGArchitect:
    def __init__(self):
        self.groq_key = os.getenv("GROQ_API_KEY")
        self.base_url = "[https://api.groq.com/openai/v1/chat/completions](https://api.groq.com/openai/v1/chat/completions)"
        self.kb_path = "knowledge_base.txt"

    def read_knowledge_base(self):
        try:
            with open(self.kb_path, "r", encoding="utf-8") as f:
                return f.read()
        except FileNotFoundError:
            return "Knowledge base file not found."

    def draft_reply(self, sender_email, email_body):
        if not self.groq_key:
            return {"error": "GROQ_API_KEY is missing."}
            
        kb_content = self.read_knowledge_base()
        
        prompt = f"""
        [ROLE] You are the digital cognitive replica of Ali Rosyid, a Senior AI Automation Architect.
        [TASK] Draft a highly technical, concise, and professional email reply to a potential B2B client (CTO/Founder) based on their incoming email and your knowledge base.
        [INPUT] 
        - Target Sender: {sender_email}
        - Incoming Email Body: {email_body}
        - Architect Knowledge Base: {kb_content}
        
        [OUTPUT] You MUST output ONLY a valid JSON object containing a single key "drafted_reply".
        [CONSTRAINTS] DO NOT output markdown tags like ```json. The tone must be authoritative, async, and technical (Frame Control). Do not offer hourly rates. Use data strictly from the Knowledge Base. If they ask a question not covered in the KB, draft a response inviting them to a 15-minute technical architecture review via Zoom/Excalidraw.
        [CAPABILITIES] Retrieval-Augmented Generation (RAG) and B2B consultative sales psychology.
        
        SCHEMA REQUIRED:
        {{
            "drafted_reply": "The exact text of the email reply..."
        }}
        """
        
        payload = {
            "model": "llama-3.3-70b-versatile",
            "messages": [{"role": "user", "content": prompt}],
            "response_format": {"type": "json_object"},
            "temperature": 0.2
        }
        
        headers = {
            "Authorization": f"Bearer {self.groq_key}",
            "Content-Type": "application/json"
        }
        
        response = requests.post(self.base_url, json=payload, headers=headers)
        
        if response.status_code != 200:
            return {"error": response.text}
            
        try:
            raw_content = response.json()['choices'][0]['message']['content']
            clean_json = json.loads(raw_content)
            return clean_json
        except Exception as e:
            return {"error": f"Failed to parse AI JSON. Error: {str(e)}"}

@app.post("/generate_reply")
async def generate_reply_endpoint(payload: IncomingEmail):
    architect = RAGArchitect()
    result = architect.draft_reply(payload.sender_email, payload.email_body)
    
    if "error" in result:
        raise HTTPException(status_code=400, detail=result["error"])
        
    return {"status": "success", "data": result}
