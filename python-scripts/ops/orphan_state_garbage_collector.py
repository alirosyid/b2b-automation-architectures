import sqlite3
import logging
import time

logger = logging.getLogger(__name__)

class OrphanStateGarbageCollector:
    """
    Stateful Infrastructure Maintenance.
    Sweeps distributed databases for 'Orphaned' execution states caused by 
    catastrophic pipeline crashes or severed async workers. Safely purges dead 
    locks and unresolvable queues to optimize query latency and reduce cloud bloat.
    """
    def __init__(self, db_path: str = "orchestration_state.db", orphan_timeout_sec: int = 3600):
        self.conn = sqlite3.connect(db_path)
        self.timeout = orphan_timeout_sec
        # Ensure target table architecture exists
        self.conn.execute('''CREATE TABLE IF NOT EXISTS active_locks 
                             (lock_id TEXT PRIMARY KEY, timestamp REAL)''')

    def execute_temporal_sweep(self) -> int:
        current_time = time.time()
        cutoff_time = current_time - self.timeout
        
        logger.info(f"Initializing Garbage Collection sweep for states preceding timestamp {cutoff_time}...")
        
        cursor = self.conn.cursor()
        cursor.execute("SELECT COUNT(*) FROM active_locks WHERE timestamp < ?", (cutoff_time,))
        orphans_detected = cursor.fetchone()[0]
        
        if orphans_detected > 0:
            logger.warning(f"Detected {orphans_detected} orphaned infrastructure locks. Executing hard purge.")
            self.conn.execute("DELETE FROM active_locks WHERE timestamp < ?", (cutoff_time,))
            self.conn.commit()
            
        logger.info("Garbage Collection sweep complete. State database optimized.")
        return orphans_detected
