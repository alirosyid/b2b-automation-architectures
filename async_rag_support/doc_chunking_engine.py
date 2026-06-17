import asyncio

class DocumentChuncker:
    def __init__(self, chunk_size=500, overlap=50):
        self.chunk_size = chunk_size
        self.overlap = overlap

    async def async_chunk_text(self, text):
        print("[RAG] Beginning asynchronous chunking process...")
        words = text.split()
        chunks = []
        
        for i in range(0, len(words), self.chunk_size - self.overlap):
            chunk = " ".join(words[i:i + self.chunk_size])
            chunks.append(chunk)
            await asyncio.sleep(0.01) # Yield control to event loop
            
        print(f"[RAG] Processed text into {len(chunks)} overlapping vectors.")
        return chunks

async def process_document_pipeline(raw_text):
    chunker = DocumentChuncker()
    vectors = await chunker.async_chunk_text(raw_text)
    return {"status": "ready_for_embedding", "total_vectors": len(vectors)}

if __name__ == "__main__":
    mock_doc = "This is a mock contract. " * 1000
    asyncio.run(process_document_pipeline(mock_doc))
