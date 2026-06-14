import re

def extract_keywords(title, description):
    combined_text = f"{title} {description}".lower()
    # Basic extraction of words longer than 4 characters
    words = re.findall(r'\b[a-z]{5,}\b', combined_text)
    
    # Simple frequency count
    keyword_freq = {}
    for word in words:
        keyword_freq[word] = keyword_freq.get(word, 0) + 1
        
    sorted_keywords = sorted(keyword_freq.items(), key=lambda x: x[1], reverse=True)
    return [kw[0] for kw in sorted_keywords[:10]]

if __name__ == "__main__":
    title = "Best AI Automations for Business 2026"
    desc = "Learn how AI automations can scale your business and generate more revenue."
    print("Tags:", extract_keywords(title, desc))
