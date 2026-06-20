def cluster_seo_keywords(keywords):
    clusters = {"Infrastructure": [], "Marketing Auth": [], "Data Processing": []}
    
    for keyword in keywords:
        kw_lower = keyword.lower()
        if "server" in kw_lower or "cloud" in kw_lower:
            clusters["Infrastructure"].append(keyword)
        elif "lead" in kw_lower or "email" in kw_lower:
            clusters["Marketing Auth"].append(keyword)
        else:
            clusters["Data Processing"].append(keyword)
            
    print("[Trends] Keywords successfully clustered for programmatic content generation.")
    return clusters

if __name__ == "__main__":
    raw_keywords = ["cloud server automation", "b2b cold email intent", "unstructured data parsing"]
    clustered = cluster_seo_keywords(raw_keywords)
    for topic, terms in clustered.items():
        if terms: print(f"- {topic}: {terms}")
