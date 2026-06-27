def generate_qbr_outline(client_name, total_workflows_run, estimated_hours_saved):
    print(f"[BizOps] Compiling 90-day metrics for {client_name} QBR...")
    
    qbr_deck_outline = f"""
    # QBR: {client_name}
    
    ## Slide 1: The Quarter in Review
    - Total Automated Workflows Executed: {total_workflows_run:,}
    - Estimated Human Hours Recovered: {estimated_hours_saved:,} hrs
    
    ## Slide 2: System Health & Uptime
    - Core infrastructure maintained 99.99% uptime.
    - Zero security breaches or data leaks.
    
    ## Slide 3: Roadmap for Next Quarter
    - Transitioning legacy REST calls to GraphQL bridging.
    - Implementing autonomous Tier-1 AI support agents.
    """
    
    print("[BizOps] QBR Outline generated. Ready for slide deck formatting.")
    return qbr_deck_outline

if __name__ == "__main__":
    print(generate_qbr_outline("Global Logistics Inc", 145000, 1200))
