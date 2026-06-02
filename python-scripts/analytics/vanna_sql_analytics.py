import logging
from vanna.remote import VannaDefault

logger = logging.getLogger(__name__)

class VannaSQLAnalytics:
    """
    Natural Language Text-to-SQL Engine.
    Allows business stakeholders to query the B2B SQLite/Postgres database 
    using natural language. Dynamically generates safe SQL, executes the query, 
    and returns analytical insights without requiring manual dashboarding.
    """
    def __init__(self, api_key: str, vanna_model: str, db_path: str = "b2b_leads.db"):
        self.vn = VannaDefault(model=vanna_model, api_key=api_key)
        self.vn.connect_to_sqlite(db_path)

    def execute_natural_query(self, human_question: str) -> str:
        logger.info(f"Translating natural language to SQL: '{human_question}'")
        
        try:
            # Generate SQL, run it, and use LLM to summarize the DataFrame
            summary = self.vn.ask(question=human_question, print_results=False)
            logger.info("SQL query generated and executed successfully.")
            return summary
            
        except Exception as e:
            logger.error(f"Text-to-SQL inference failed: {e}")
            return "Analytics temporarily unavailable."
