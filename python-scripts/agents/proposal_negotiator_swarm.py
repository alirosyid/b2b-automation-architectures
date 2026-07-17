def execute_counter_offer_negotiation(original_price, counter_offer, original_scope):
    print("[Swarm] Intercepted prospect counter-offer. Initiating Multi-Agent Negotiation...")
    
    margin_agent_decision = counter_offer / original_price
    
    if margin_agent_decision > 0.75: # They offered at least 75% of original price
        print("    -> Margin Agent: Counter-offer acceptable. Recalculating scope.")
        
        # Scope Agent removes least critical feature
        revised_scope = original_scope[:-1] 
        print(f"    -> Scope Agent: Removed '{original_scope[-1]}' to maintain 60% profit margin.")
        
        draft_agent = f"We can meet your budget at ${counter_offer}. To make the math work, we will phase out the {original_scope[-1]} module for now. Deal?"
        
        print("[+] Optimal counter-proposal generated and routed to outbound queue.")
        return draft_agent
        
    print("[-] Counter-offer below margin threshold. Escalating to human Sales Director.")
    return None

if __name__ == "__main__":
    execute_counter_offer_negotiation(10000, 8000, ["HubSpot Sync", "Slack Bot", "Custom Dashboard"])
