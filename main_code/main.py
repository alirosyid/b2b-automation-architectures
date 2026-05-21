import os
import json
import requests
import io
from fastapi import FastAPI, HTTPException, File, UploadFile
from pydantic import BaseModel
from dotenv import load_dotenv
from PIL import Image
import google.generativeai as genai

# =====================================================================
# INISIALISASI ENVIRONMENT & APLIKASI UTAMA
# =====================================================================
load_dotenv()

app = FastAPI(title="Ali Rosyid - Enterprise B2B AI Gateway")

GROQ_API_KEY = os.getenv("GROQ_API_KEY")
GROQ_URL = "https://api.groq.com/openai/v1/chat/completions"

# =====================================================================
# DATA SCHEMAS (PYDANTIC MODELS UNTUK LOKET 1, 2, 3)
# =====================================================================
class Payload(BaseModel):
    company_data: str

class JobPayload(BaseModel):
    job_description: str

class ReplyPayload(BaseModel):
    sender_email: str
    email_body: str

# =====================================================================
# CORE LLM INFERENCE HELPER (GATEWAY ENGINE - GROQ)
# =====================================================================
def call_llama_gateway(prompt: str) -> dict:
    if not GROQ_API_KEY:
        raise HTTPException(status_code=500, detail="GROQ_API_KEY tidak ditemukan di file .env")
        
    headers = {
        "Authorization": f"Bearer {GROQ_API_KEY}",
        "Content-Type": "application/json"
    }
    
    payload = {
        "model": "llama-3.3-70b-versatile",
        "messages": [{"role": "user", "content": prompt}],
        "temperature": 0.1
    }
    
    try:
        response = requests.post(GROQ_URL, headers=headers, json=payload)
        response.raise_for_status()
        res_json = response.json()
        
        content = res_json["choices"][0]["message"]["content"].strip()
        
        if content.startswith("```json"):
            content = content.replace("```json", "", 1).rstrip("```").strip()
        elif content.startswith("```"):
            content = content.replace("```", "", 1).rstrip("```").strip()
            
        return json.loads(content)
        
    except requests.exceptions.RequestException as e:
        raise HTTPException(status_code=502, detail=f"Groq API Error: {str(e)}")
    except json.JSONDecodeError:
        raise HTTPException(status_code=502, detail="Gagal melakukan parsing JSON dari output AI.")

# =====================================================================
# LOKET 1: JALUR A - THE SNIPER (B2B Lead Enrichment / Scraped Website)
# Endpoint: POST http://localhost:8000/enrich
# =====================================================================
@app.post("/enrich")
async def enrich_lead(payload: Payload):
    prompt = f"""
    You are a world-class B2B IT Automation Architect. Analyze the following raw scraped website data to extract the company name, primary business industry, and identify exactly 3 critical technical or operational bottlenecks they are likely facing, along with their business impacts.
    
    Scraped Data:
    {payload.company_data}
    
    You MUST respond ONLY with a valid raw JSON object matching this exact structure. Do not include markdown formatting like ```json or any conversational text.
    
    {{
      "status": "success",
      "ai_analysis": {{
        "company": "Extract Real Company Name",
        "business_category": "Extract Industry Category",
        "bottlenecks": [
          {{
            "issue": "Identify critical technical bottleneck 1",
            "business_impact": "The financial or operational impact if unresolved"
          }},
          {{
            "issue": "Identify critical technical bottleneck 2",
            "business_impact": "The financial or operational impact if unresolved"
          }},
          {{
            "issue": "Identify critical technical bottleneck 3",
            "business_impact": "The financial or operational impact if unresolved"
          }}
        ]
      }}
    }}
    """
    return call_llama_gateway(prompt)

# =====================================================================
# LOKET 2: JALUR B - THE SNIPER (Job Board Description Analysis)
# Endpoint: POST http://localhost:8000/analyze_job
# =====================================================================
@app.post("/analyze_job")
async def analyze_job(payload: JobPayload):
    prompt = f"""
    You are an expert Enterprise Sales Strategist. Analyze the following official job description to extract the company name, their primary engineering/business category, and deduce the exact systemic bottlenecks or pain points they are trying to solve by hiring for this position.
    
    Job Description:
    {payload.job_description}
    
    You MUST respond ONLY with a valid raw JSON object matching this exact structure. Do not include markdown formatting like ```json or any conversational text.
    
    {{
      "status": "success",
      "ai_analysis": {{
        "company": "Extract Company Name from job description, if unknown use 'Valued Prospect'",
        "business_category": "Extract core engineering/business category",
        "bottlenecks": [
          {{
            "issue": "Deduce the core technical bottleneck they are hiring to fix based on requirements",
            "business_impact": "The risk or financial cost to their operation if this position remains unfilled"
          }}
        ]
      }}
    }}
    """
    return call_llama_gateway(prompt)

# =====================================================================
# LOKET 3: THE DEFENDER (Telegram RAG Email Responder)
# Endpoint: POST http://localhost:8000/generate_reply
# =====================================================================
@app.post("/generate_reply")
async def generate_reply(payload: ReplyPayload):
    try:
        kb_path = "knowledge_base.txt"
        if os.path.exists(kb_path):
            with open(kb_path, "r", encoding="utf-8") as file:
                knowledge_base = file.read()
        else:
            knowledge_base = "Informasi tidak ditemukan. Gunakan nada profesional standar."

        prompt = f"""
        You are the personal AI Assistant for Ali Rosyid, a Senior AI Automation Architect.
        A prospective client has just replied to our cold outreach email.
        
        Client Email ({payload.sender_email}):
        "{payload.email_body}"
        
        Ali's Internal Rules & Profile (Knowledge Base):
        {knowledge_base}
        
        Task: Draft a professional, confident reply based strictly on Ali's Knowledge Base. 
        If the client asks for hourly rates, firmly decline and state Ali only does project-based or retainer contracts.
        
        You MUST respond ONLY with a raw JSON object matching this exact structure:
        {{
          "status": "success",
          "client_intent": "Briefly summarize what the client wants",
          "draft_reply": "The exact email text Ali should send back to the client"
        }}
        """
        return call_llama_gateway(prompt)
        
    except Exception as e:
        return {"status": "error", "message": str(e)}

# =====================================================================
# LOKET 4: THE VISIONARY (AI OCR Document Extraction via Native Multipart)
# Endpoint: POST http://localhost:8000/ocr
# =====================================================================
@app.post("/ocr")
async def process_document(file: UploadFile = File(...)):
    # Tolak jika file bukan gambar
    if not file.content_type.startswith("image/"):
        raise HTTPException(status_code=400, detail="Invalid file type. Must be an image.")

    api_key = os.getenv("GEMINI_API_KEY")
    if not api_key:
        raise HTTPException(status_code=500, detail="GEMINI_API_KEY tidak ditemukan di file .env")

    try:
        # Konfigurasi & Inisialisasi Mesin Utama Gemini (Versi 2.5)
        genai.configure(api_key=api_key)
        model = genai.GenerativeModel('gemini-2.5-flash')
        
        # Membaca file fisik langsung dari n8n
        contents = await file.read()
        image = Image.open(io.BytesIO(contents))
        
        # Prompt pengekstrakan presisi tinggi tanpa gangguan markdown
        prompt = """
        Ekstrak data dari dokumen ini ke JSON murni. 
        DILARANG KERAS pakai markdown ataupun text pembuka.
        Struktur output: {'Vendor_Name': 'str', 'Invoice_Number': 'str', 'Date': 'YYYY-MM-DD', 'Total_Amount': number, 'Line_Items': [{'item_name': 'str', 'price': number}]}. 
        Jika data kosong atau tidak ditemukan, isi dengan null.
        """
        
        response = model.generate_content([prompt, image])
        raw_text = response.text
        
        # Pembersihan paksa jika model mengembalikan tag ```json
        clean_text = raw_text.replace('```json', '').replace('```', '').strip()
        
        return {
            "status": "success",
            "extracted_data": json.loads(clean_text)
        }
        
    except Exception as e:
        return {"status": "error", "message": str(e)}
