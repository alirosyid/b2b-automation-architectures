import os
from PyPDF2 import PdfReader
from openai import OpenAI

def score_contract_risk(pdf_path, llm_client):
    """Parses a B2B contract PDF and highlights high-risk clauses using an LLM."""
    reader = PdfReader(pdf_path)
    contract_text = "".join([page.extract_text() for page in reader.pages])
    
    prompt = f"""
    Analyze the following B2B contract. Identify any high-risk clauses, 
    unfavorable liability caps, or auto-renewal traps. 
    Format the output as a JSON with a 'risk_score' (1-10) and 'warnings'.
    Contract: {contract_text[:15000]} # Truncated for context window limits
    """
    
    response = llm_client.chat.completions.create(
        model="gpt-4o",
        messages=[{"role": "system", "content": "You are an expert corporate lawyer."},
                  {"role": "user", "content": prompt}],
        response_format={ "type": "json_object" }
    )
    
    return response.choices[0].message.content

if __name__ == "__main__":
    client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))
    risk_assessment = score_contract_risk("/legal_docs/vendor_agreement.pdf", client)
    print("Contract Risk Assessment:\n", risk_assessment)
