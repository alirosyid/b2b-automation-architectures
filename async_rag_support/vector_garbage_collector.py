def prune_stale_vectors(vector_database_metadata, days_old_threshold=90):
    import datetime
    
    current_time = datetime.datetime.now()
    pruned_count = 0
    
    for vector_id, metadata in vector_database_metadata.items():
        last_accessed = metadata.get("last_accessed")
        age_days = (current_time - last_accessed).days
        
        if age_days > days_old_threshold:
            print(f"[RAG] 🗑️ Pruning stale vector {vector_id} (Age: {age_days} days).")
            # Mock DB delete action
            pruned_count += 1
            
    print(f"[RAG] Garbage collection complete. Removed {pruned_count} outdated vectors.")
    return pruned_count

if __name__ == "__main__":
    import datetime
    mock_db = {
        "vec_001": {"last_accessed": datetime.datetime.now() - datetime.timedelta(days=100)},
        "vec_002": {"last_accessed": datetime.datetime.now() - datetime.timedelta(days=10)}
    }
    prune_stale_vectors(mock_db)
