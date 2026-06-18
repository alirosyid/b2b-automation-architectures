from collections import defaultdict

def cluster_keywords(keyword_list):
    clusters = defaultdict(list)
    
    # Basic matching logic (in production, use NLP embeddings like sentence-transformers)
    for kw in keyword_list:
        if "ai" in kw or "automation" in kw:
            clusters["AI & Automation"].append(kw)
        elif "b2b" in kw or "sales" in kw:
            clusters["B2B Sales"].append(kw)
        else:
            clusters["General Tech"].append(kw)
            
    return dict(clusters)

if __name__ == "__main__":
    raw_kws = ["ai marketing tools", "b2b sales strategies", "workflow automation software", "enterprise tech trends"]
    clustered_data = cluster_keywords(raw_kws)
    for topic, keywords in clustered_data.items():
        print(f"Pillar: {topic} -> {keywords}")
