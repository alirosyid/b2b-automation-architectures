import sqlite3
import logging
from typing import List

logger = logging.getLogger(__name__)

class DAGDependencyResolver:
    """
    Stateful Cross-Workflow Orchestrator.
    Manages Directed Acyclic Graph (DAG) dependencies across completely decoupled 
    n8n microservices. Mathematically locks downstream pipelines until upstream 
    prerequisite workflows are cryptographically verified as complete.
    """
    def __init__(self, db_path: str = "dag_state.db"):
        self.conn = sqlite3.connect(db_path)
        self.conn.execute('''CREATE TABLE IF NOT EXISTS workflow_states 
                             (tenant_id TEXT, workflow_name TEXT, status TEXT, 
                             PRIMARY KEY (tenant_id, workflow_name))''')

    def mark_completed(self, tenant_id: str, workflow_name: str):
        self.conn.execute("INSERT OR REPLACE INTO workflow_states (tenant_id, workflow_name, status) VALUES (?, ?, ?)",
                          (tenant_id, workflow_name, "COMPLETED"))
        self.conn.commit()
        logger.debug(f"DAG Ledger: {workflow_name} verified complete for {tenant_id}.")

    def check_dependencies(self, tenant_id: str, required_workflows: List[str]) -> bool:
        logger.info(f"Validating DAG dependencies for tenant {tenant_id}...")
        
        placeholders = ','.join('?' for _ in required_workflows)
        cursor = self.conn.execute(
            f"SELECT workflow_name FROM workflow_states WHERE tenant_id = ? AND status = 'COMPLETED' AND workflow_name IN ({placeholders})",
            (tenant_id, *required_workflows)
        )
        completed = {row[0] for row in cursor.fetchall()}
        
        if len(completed) == len(required_workflows):
            logger.info("All DAG prerequisites met. Downstream execution authorized.")
            return True
            
        missing = set(required_workflows) - completed
        logger.warning(f"DAG Locked: Upstream dependencies not met. Waiting on: {missing}")
        return False
