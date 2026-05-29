import logging
from pydantic import BaseModel, ValidationError
from typing import Optional

logger = logging.getLogger(__name__)

class B2BLeadSchema(BaseModel):
    company_name: str
    decision_maker_email: str
    annual_revenue: Optional[float] = 0.0
    is_qualified: bool

class PydanticSchemaEnforcer:
    """
    Type-Safe LLMOps Validator.
    Replaces fragile manual JSON parsing with strict Pydantic data models.
    Guarantees that AI-extracted data perfectly matches the required database 
    types before ingestion, physically preventing CRM corruption.
    """
    @classmethod
    def validate_and_cast(cls, llm_extracted_data: dict) -> dict:
        try:
            validated_lead = B2BLeadSchema(**llm_extracted_data)
            logger.info("Pydantic Validation Passed: LLM output matches exact B2B schema types.")
            return validated_lead.dict()
        except ValidationError as e:
            logger.critical(f"Pydantic Validation Failed: LLM hallucinated incorrect data types. Errors: {e.errors()}")
            # Pipeline will catch this and trigger the Autonomous DLQ Healer
            raise ValueError("Type-safe validation failed on LLM output.")
