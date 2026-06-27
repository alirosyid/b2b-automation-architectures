import re

def compress_context_payload(raw_text):
    print(f"[*] Original context length: {len(raw_text)} characters.")
    
    # Removes redundant whitespace, filler words, and stop words
    compressed = re.sub(r'\s+', ' ', raw_text)
    filler_words = ["basically", "essentially", "in order to", "as a matter of fact"]
    
    for word in filler_words:
        compressed = compressed.replace(word, "")
        
    print(f"[Core] Compressed context length: {len(compressed)} characters.")
    savings = 100 - ((len(compressed) / len(raw_text)) * 100)
    print(f"[+] Estimated Token Savings: {savings:.1f}%")
    
    return compressed.strip()

if __name__ == "__main__":
    sample_doc = "This is essentially a document that, in order to function, basically requires a lot of text." * 50
    compress_context_payload(sample_doc)
