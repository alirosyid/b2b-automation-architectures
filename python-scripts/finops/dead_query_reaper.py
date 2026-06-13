import logging

class DeadQueryReaper:
    def __init__(self, max_execution_minutes: int = 15):
        self.max_duration = max_execution_minutes

    def sweep_database_dry_run(self, active_queries: list[dict]):
        logging.info(f"[PORTFOLIO MOCK] Sweeping data warehouse for hanging queries > {self.max_duration} mins.")
        
        reaped_count = 0
        for query in active_queries:
            if query.get("duration_minutes", 0) > self.max_duration:
                logging.warning(f"[FINOPS ALERT] Hanging query detected: {query['job_id']}.")
                logging.info(f"[FINOPS MOCK] Executing KILL syntax. Preventing further billing leak.")
                reaped_count += 1
                
        logging.info(f"[FINOPS MOCK] Sweep complete. Reaped {reaped_count} dead queries. ROI protected.")
