from typing import Dict, Any

class B2BLeadScorer:
    """
    Evaluates extracted prospects to prioritize high-value outreach.
    """
    TIER_1_KEYWORDS = ["CEO", "Founder", "Director of Engineering", "CTO"]
    TIER_2_KEYWORDS = ["Manager", "Lead", "Architect"]

    @classmethod
    def calculate_score(cls, prospect_data: Dict[str, Any]) -> int:
        score = 0
        title = prospect_data.get("job_title", "").title()

        if any(kw in title for kw in cls.TIER_1_KEYWORDS):
            score += 50
        elif any(kw in title for kw in cls.TIER_2_KEYWORDS):
            score += 25

        if prospect_data.get("company_size", 0) > 100:
            score += 20

        return score
