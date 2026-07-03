import os
import pandas as pd
from openai import OpenAI

def auto_answer_rfp(excel_path, rag_retriever, llm_client):
    """Parses an RFP Excel file and automatically answers technical/security questions."""
    df = pd.read_excel(excel_path)
    
    responses = []
    for index, row in df.iterrows():
        question = row['Question']
        # Retrieve internal company knowledge
        context = rag_retriever.search(question, top_k=3)
        
        prompt = f"""
        You are a VP of Sales Engineering. Answer this RFP question professionally 
        using ONLY the provided context. If the context doesn't have the answer, 
        reply "REQUIRES_HUMAN_REVIEW".
        Question: {question}
        Context: {context}
        """
        
        response = llm_client.chat.completions.create(
            model="gpt-4o",
            messages=[{"role": "user", "content": prompt}]
        )
        responses.append(response.choices[0].message.content)
        
    df['AI_Generated_Answer'] = responses
    output_path = excel_path.replace(".xlsx", "_AI_Answered.xlsx")
    df.to_excel(output_path, index=False)
    print(f"RFP processing complete. Saved to {output_path}")

# Note: Assumes rag_retriever is initialized elsewhere in the pipeline.
