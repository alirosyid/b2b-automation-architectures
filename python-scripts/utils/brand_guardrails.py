class OutputGuardrail:
    """
    Validates LLM-generated content against B2B brand safety rules 
    before sending via email or Telegram.
    """
    RESTRICTED_TOPICS = ["politics", "religion", "competitor_bashing", "unrealistic_promises"]

    @classmethod
    def validate_outreach_email(cls, generated_text: str) -> bool:
        text_lower = generated_text.lower()

        for topic in cls.RESTRICTED_TOPICS:
            # In production, this uses a lightweight classifier model
            if topic in text_lower:
                return False

        # Check for excessive promotional tone
        if text_lower.count("!") > 3:
            return False

        return True
