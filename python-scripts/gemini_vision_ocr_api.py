import os
import io
import json
from fastapi import FastAPI, File, UploadFile
from PIL import Image
import google.generativeai as genai
from dotenv import load_dotenv

load_dotenv()

API_KEY = os.getenv("GEMINI_API_KEY")

if API_KEY:
    os.environ["GOOGLE_API_KEY"] = API_KEY

genai.configure(api_key=API_KEY)

app = FastAPI()
model = genai.GenerativeModel("gemini-2.5-flash")

@app.get("/")
def ping():
    return {"status": "Mesin API Hidup!"}

@app.post("/extract-invoice")
async def extract_invoice(file: UploadFile = File(...)):
    try:
        contents = await file.read()
        image = Image.open(io.BytesIO(contents))
        
        prompt = 'Ekstrak data dari dokumen ini. CONSTRAINTS: 1. Output WAJIB dalam format JSON murni. 2. DILARANG menggunakan markdown. 3. Gunakan struktur: {"Vendor_Name": "string", "Invoice_Number": "string", "Date": "YYYY-MM-DD", "Total_Amount": number, "Line_Items": [{"item_name": "string", "price": number}]}. Jika kosong, isi null.'
        
        response = model.generate_content([prompt, image])
        raw_text = response.text.replace('```json', '').replace('```', '').strip()
        return json.loads(raw_text)
    except Exception as e:
        return {"STATUS": "ERROR", "DETAIL": str(e)}
