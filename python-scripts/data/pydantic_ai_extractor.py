import logging
from pydantic import BaseModel, Field
from pydantic_ai import Agent

logger = logging.getLogger(__name__)

class B2BLeadProfile(BaseModel):
    company_name: str
    decision_maker_role: str
    estimated_revenue_usd: int = Field(description="Strict integer extraction of revenue")
    is_b2b_saas: bool

class PydanticAIExtractor:
    """
    Type-Safe Extraction Engine.
    Leverages PydanticAI to enforce strict structural schemas on LLM outputs.
    Guarantees that unstructured web data is perfectly typed before CRM ingestion.
    """
    def __init__(self):
        # Configured for Groq's high-speed Llama-3 endpoint
        self.agent = Agent('groq:llama3-70b-8192', result_type=B2BLeadProfile)

    def extract_lead_data(self, unstructured_web_text: str) -> B2BLeadProfile:
        logger.info("Executing PydanticAI type-safe extraction...")
        
        result = self.agent.run_sync(
            f"Extract the company profile from this text: {unstructured_web_text}"
        )
        
        logger.info(f"Extraction successful. Mathematically validated schema for: {result.data.company_name}")
        return result.data
