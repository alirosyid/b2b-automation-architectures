import logging
from collections import Counter
from typing import List, Any

logger = logging.getLogger(__name__)

class MultiAgentConsensusEngine:
    """
    Enterprise 'Mixture of Agents' (MoA) Orchestrator.
    Prevents catastrophic hallucinations during high-stakes B2B pipeline actions
    (e.g., qualifying a Fortune 500 lead or triggering automated invoices) by requiring 
    a democratic consensus from multiple distinct LLM evaluations before executing a CRM mutation.
    """
    def __init__(self, required_agreement_threshold: int = 2):
        self.threshold = required_agreement_threshold

    def evaluate_high_stakes_decision(self, agent_responses: List[Any]) -> dict:
        logger.info(f"Initiating consensus evaluation across {len(agent_responses)} independent agent nodes.")

        # Count the frequency of each distinct decision
        decision_counts = Counter(str(response) for response in agent_responses)
        agreed_decision, votes = decision_counts.most_common(1)[0]

        if votes >= self.threshold:
            logger.info(f"Consensus reached: {votes}/{len(agent_responses)} agents agreed on the output.")
            return {
                "status": "execution_approved", 
                "consensus_output": agreed_decision, 
                "confidence_score": round(votes / len(agent_responses), 2)
            }

        logger.critical(f"Consensus Failed. Maximum agreement was {votes}. Escalating to Human-in-the-Loop QA.")
        # Production: Trigger n8n webhook to Slack/Teams for human review
        return {"status": "escalated_to_human", "reason": "agent_disagreement"}
