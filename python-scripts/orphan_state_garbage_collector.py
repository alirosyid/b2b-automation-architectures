import sqlite3
import logging

def execute_garbage_collection(db_path: str):
    """
    SRE routine to self-heal storage limits and prevent degraded search performance
    in the GraphRAG pipeline by purging orphaned transactional states.
    """
    try:
        conn = sqlite3.connect(db_path)
        cursor = conn.cursor()
        
        # Identify nodes with no relational edges older than 72 hours
        purge_query = """
            DELETE FROM rag_memory_states 
            WHERE edge_count = 0 
            AND last_accessed < datetime('now', '-3 days')
        """
        cursor.execute(purge_query)
        rows_deleted = cursor.rowcount
        conn.commit()
        
        logging.info(f"[SRE OPTIMIZATION] Vacuumed {rows_deleted} orphaned memory states. Reclaiming storage.")
        
        # Optimize remaining indexing
        cursor.execute("VACUUM;")
    except Exception as e:
        logging.error(f"[SRE FATAL] Garbage collection failed: {str(e)}")
    finally:
        conn.close()
