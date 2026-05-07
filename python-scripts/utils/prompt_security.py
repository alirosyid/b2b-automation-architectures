import re
import logging

logger = logging.getLogger(__name__)

class PromptInjectionDefender:
    """
    Memfilter input pengguna sebelum dikirim ke Groq/Gemini untuk mencegah
    serangan Prompt Injection yang dapat merusak agen RAG klien.
    """
    BLOCKED_PATTERNS = [
        r"(?i)ignore previous instructions",
        r"(?i)system prompt",
        r"(?i)bypass restrictions",
        r"(?i)forget everything"
    ]

    @classmethod
    def sanitize_input(cls, user_input: str) -> str:
        for pattern in cls.BLOCKED_PATTERNS:
            if re.search(pattern, user_input):
                logger.warning(f"SECURITY ALERT: Prompt injection attempt blocked. Input: {user_input}")
                return "I am a professional B2B assistant. I cannot process that request."
        return user_input
