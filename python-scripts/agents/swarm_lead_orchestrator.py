import logging
from swarm import Swarm, Agent

logger = logging.getLogger(__name__)

class SwarmLeadOrchestrator:
    """
    Multi-Agent Handoff Architecture.
    Utilizes lightweight Swarm framework to decouple B2B tasks.
    A Researcher agent gathers data and autonomously hands off execution 
    to a Sales agent for personalized outreach generation.
    """
    def __init__(self):
        self.client = Swarm()
        
        self.sales_agent = Agent(
            name="B2B Sales Closer",
            instructions="Write a high-converting, 3-sentence B2B outreach email based on the provided company data."
        )
        
        self.research_agent = Agent(
            name="B2B Lead Researcher",
            instructions="Extract the core business model from the input. Then hand off to the Sales Closer.",
            functions=[self.transfer_to_sales]
        )

    def transfer_to_sales(self):
        logger.info("Agent Handoff: Research complete. Transferring state to Sales Closer.")
        return self.sales_agent

    def execute_swarm(self, company_description: str) -> str:
        logger.info("Initializing Swarm Multi-Agent execution...")
        response = self.client.run(
            agent=self.research_agent,
            messages=[{"role": "user", "content": company_description}]
        )
        return response.messages[-1]["content"]
