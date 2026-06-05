```python
from pydantic import BaseModel, ValidationError, EmailStr
from typing import Optional
import logging

logger = logging.getLogger(__name__)

class B2BLeadSchema(BaseModel):
    """
    Strict schema validation for AI-enriched B2B leads.
    """
    company_name: str
    decision_maker_name: str
    email: EmailStr
    industry: str
    ai_confidence_score: float
    summary: Optional[str] = None

def validate_lead_data(raw_data: dict) -> dict:
    try:
        validated = B2BLeadSchema(**raw_data)
        return validated.dict()
    except ValidationError as e:
        logger.error(f"LLM output failed validation: {e.errors()}")
        raise ValueError("Invalid data structure from LLM.")
