import json
import os

def inject_business_context(active_tickets):
    print("[DevOps] Injecting live business requirements into GitHub Copilot Workspace...")
    instructions = "# Active Business Context\n"
    
    for ticket in active_tickets:
        instructions += f"- {ticket['id']}: {ticket['description']}\n"
    
    # Writing context to Copilot's hidden instruction file
    with open(".github/copilot-instructions.md", "w") as f:
        f.write(instructions)
        
    print("[+] Copilot context perfectly aligned with current sprint goals.")
    return True

if __name__ == "__main__":
    mock_tickets = [{"id": "B2B-102", "description": "Implement strictly typed JSON schema validation for inbound leads."}]
    inject_business_context(mock_tickets)
