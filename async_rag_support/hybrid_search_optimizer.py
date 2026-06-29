def execute_hybrid_search(user_query, semantic_db, keyword_db, alpha=0.5):
    print(f"[RAG] Executing hybrid search for query: '{user_query}'")
    
    # Mock retrieval results
    semantic_results = {"doc_1": 0.88, "doc_3": 0.75}
    keyword_results = {"doc_1": 0.50, "doc_2": 0.90}
    
    hybrid_scores = {}
    all_docs = set(semantic_results.keys()).union(set(keyword_results.keys()))
    
    for doc in all_docs:
        s_score = semantic_results.get(doc, 0)
        k_score = keyword_results.get(doc, 0)
        # Reciprocal Rank Fusion (RRF) simplified logic
        hybrid_scores[doc] = (alpha * s_score) + ((1 - alpha) * k_score)
        
    best_doc = max(hybrid_scores, key=hybrid_scores.get)
    print(f"[+] Optimal document retrieved via Hybrid Search: {best_doc} (Score: {hybrid_scores[best_doc]:.2f})")
    
    return best_doc

if __name__ == "__main__":
    execute_hybrid_search("How to configure API rate limits", {}, {})
