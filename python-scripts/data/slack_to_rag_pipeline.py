import os
from openai import OpenAI

def extract_and_embed_slack_knowledge(thread_messages, pinecone_index, llm_client):
    """Summarizes a resolved Slack thread and pushes it to the RAG Vector DB."""
    raw_thread = " ".join([msg['text'] for msg in thread_messages])
    
    prompt = f"Summarize this resolved technical issue into a clean 'Problem' and 'Solution' format for a knowledge base: {raw_thread}"
    
    response = llm_client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[{"role": "user", "content": prompt}]
    )
    
    kb_entry = response.choices[0].message.content
    
    # Generate Embedding
    embedding = llm_client.embeddings.create(input=[kb_entry], model="text-embedding-3-small").data[0].embedding
    
    # Push to Vector DB
    pinecone_index.upsert(vectors=[{"id": f"slack_thread_{thread_messages[0]['ts']}", "values": embedding, "metadata": {"text": kb_entry}}])
    print("New knowledge successfully embedded into Vector DB.")

# Event listener triggers would pass 'thread_messages' here.
