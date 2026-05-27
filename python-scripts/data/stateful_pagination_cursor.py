import sqlite3
import logging
from typing import Optional

logger = logging.getLogger(__name__)

class StatefulPaginationCursor:
    """
    Big Data ETL Resilience Engine.
    Tracks exact API pagination offsets during massive B2B data syncs. 
    Enables autonomous pipeline resumption from the exact point of failure, 
    preventing duplicate API compute and ensuring zero data loss.
    """
    def __init__(self, db_path: str = "pagination_state.db"):
        self.conn = sqlite3.connect(db_path)
        self.conn.execute('''CREATE TABLE IF NOT EXISTS sync_cursors 
                             (sync_job_id TEXT PRIMARY KEY, current_page INTEGER, next_page_token TEXT)''')

    def save_cursor(self, sync_job_id: str, current_page: int, next_page_token: str):
        self.conn.execute(
            "INSERT OR REPLACE INTO sync_cursors (sync_job_id, current_page, next_page_token) VALUES (?, ?, ?)",
            (sync_job_id, current_page, next_page_token)
        )
        self.conn.commit()
        logger.debug(f"Cursor saved for job {sync_job_id}: Page {current_page}.")

    def retrieve_cursor(self, sync_job_id: str) -> Optional[dict]:
        cursor = self.conn.execute(
            "SELECT current_page, next_page_token FROM sync_cursors WHERE sync_job_id = ?", 
            (sync_job_id,)
        )
        record = cursor.fetchone()
        
        if record:
            logger.info(f"Resuming job {sync_job_id} from Page {record[0]}.")
            return {"page": record[0], "token": record[1]}
            
        logger.info(f"No existing cursor found for {sync_job_id}. Starting fresh sync.")
        return None

    def clear_cursor(self, sync_job_id: str):
        self.conn.execute("DELETE FROM sync_cursors WHERE sync_job_id = ?", (sync_job_id,))
        self.conn.commit()
        logger.info(f"Sync job {sync_job_id} complete. Cursor successfully cleared.")
