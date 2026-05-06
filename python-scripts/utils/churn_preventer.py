class ChurnPreventionSystem:
    """
    Menganalisis balasan prospek/klien. Jika terdeteksi sentimen negatif tingkat tinggi,
    langsung eskalasi ke Telegram/Slack manusia untuk intervensi manual (Human-in-the-Loop).
    """
    HIGH_RISK_KEYWORDS = ["cancel", "angry", "stop", "unsubscribe", "lawyer", "spam"]

    @classmethod
    def analyze_reply(cls, email_body: str) -> dict:
        body_lower = email_body.lower()
        risk_score = sum(1 for word in cls.HIGH_RISK_KEYWORDS if word in body_lower)

        if risk_score >= 2:
            return {"status": "ESCALATE_TO_HUMAN", "reason": "High churn risk detected"}
        return {"status": "AUTO_REPLY", "reason": "Normal sentiment"}
