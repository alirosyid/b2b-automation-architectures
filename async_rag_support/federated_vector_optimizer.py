def route_federated_vector_query(user_query):
    print("[RAG Ops] Analyzing semantic intent for Federated Vector Routing...")
    
    query_lower = user_query.lower()
    
    # Intent classification for federated routing
    if "clause" in query_lower or "liability" in query_lower:
        target_db = "vector_db_legal_contracts"
        print("[+] Legal intent isolated. Bypassing general knowledge base.")
    elif "api" in query_lower or "endpoint" in query_lower:
        target_db = "vector_db_technical_docs"
        print("[+] Technical intent isolated. Bypassing general knowledge base.")
    else:
        target_db = "vector_db_general_onboarding"
        
    print(f"    -> Dispatching optimized query exclusively to: {target_db}")
    return target_db

if __name__ == "__main__":
    route_federated_vector_query("What is the liability cap in the standard MSA?")
