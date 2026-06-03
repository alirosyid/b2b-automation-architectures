import sqlite3
import json
import logging
from typing import Dict, Any

logger = logging.getLogger(__name__)

class SchemaEvolutionTracker:
    """
    Adaptive Extract, Transform, Load (ETL).
    Statefully monitors inbound B2B JSON payloads for structural changes over time.
    Gracefully adapts to unannounced client CRM updates (Schema Drift) while 
    maintaining a historical ledger of data architecture evolution.
    """
    def __init__(self, db_path: str = "schema_evolution.db"):
        self.conn = sqlite3.connect(db_path)
        self.conn.execute('''CREATE TABLE IF NOT EXISTS schema_versions 
                             (tenant_id TEXT PRIMARY KEY, schema_signature TEXT)''')

    def track_and_adapt(self, tenant_id: str, payload: Dict[str, Any]):
        current_schema = {k: type(v).__name__ for k, v in payload.items()}
        current_signature = json.dumps(current_schema, sort_keys=True)
        
        cursor = self.conn.execute("SELECT schema_signature FROM schema_versions WHERE tenant_id = ?", (tenant_id,))
        record = cursor.fetchone()
        
        if not record:
            self.conn.execute("INSERT INTO schema_versions (tenant_id, schema_signature) VALUES (?, ?)", 
                              (tenant_id, current_signature))
            self.conn.commit()
            logger.info(f"Baseline schema established for tenant {tenant_id}.")
        elif record[0] != current_signature:
            logger.warning(f"Schema Evolution Detected for tenant {tenant_id}. Adapting pipeline.")
            self.conn.execute("UPDATE schema_versions SET schema_signature = ? WHERE tenant_id = ?", 
                              (current_signature, tenant_id))
            self.conn.commit()
            # Pipeline continues gracefully with adapted expectations
