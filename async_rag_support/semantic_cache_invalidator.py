def invalidate_stale_cache(document_id, semantic_cache_keys):
    print(f"[RAG Ops] Source document update detected for {document_id}.")
    print("[RAG Ops] Scanning semantic cache for dependent vector embeddings...")
    
    invalidated_count = 0
    for key in semantic_cache_keys:
        if document_id in key:
            print(f"    🗑️ Dropping stale cache node: {key}")
            invalidated_count += 1
            # Mocking Redis / Memcached deletion
            
    if invalidated_count > 0:
        print(f"[+] Cache invalidation complete. {invalidated_count} stale responses purged.")
        print("    -> AI will regenerate fresh responses from the updated document.")
    else:
        print("[+] No stale cache nodes found.")
        
    return invalidated_count

if __name__ == "__main__":
    mock_keys = ["query_hash_x9a_doc_44", "query_hash_b2c_doc_99", "query_hash_111_doc_44"]
    invalidate_stale_cache("doc_44", mock_keys)
