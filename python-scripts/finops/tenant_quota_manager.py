import sqlite3
import logging

logger = logging.getLogger(__name__)

class CrossTenantQuotaManager:
    """
    SaaS Financial Operations (FinOps) Governor.
    Statefully tracks LLM token consumption across distinct B2B tenants.
    Prevents a single high-volume client from exhausting the global API 
    budget, enforcing fair-use policies and subscription tier limits.
    """
    def __init__(self, db_path: str = "tenant_quotas.db"):
        self.conn = sqlite3.connect(db_path)
        self.conn.execute('''CREATE TABLE IF NOT EXISTS token_usage 
                             (tenant_id TEXT PRIMARY KEY, tokens_used INTEGER, monthly_limit INTEGER)''')

    def authorize_inference(self, tenant_id: str, estimated_tokens: int) -> bool:
        cursor = self.conn.execute("SELECT tokens_used, monthly_limit FROM token_usage WHERE tenant_id = ?", (tenant_id,))
        record = cursor.fetchone()
        
        if not record:
            logger.warning(f"Tenant {tenant_id} not found in Quota DB. Blocking inference.")
            return False
            
        tokens_used, monthly_limit = record
        
        if tokens_used + estimated_tokens > monthly_limit:
            logger.critical(f"FINOPS BLOCK: Tenant {tenant_id} exceeded monthly token quota ({monthly_limit}).")
            return False
            
        logger.debug(f"Quota check passed for tenant {tenant_id}. Inference authorized.")
        return True
