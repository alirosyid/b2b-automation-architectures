def generate_stealth_case_study(client_industry, hours_saved, roi_multiplier):
    template = f"""
    # Automation Impact Report: {client_industry} Sector
    
    ## The Bottleneck
    A leading enterprise in the {client_industry} space was losing critical momentum due to manual data routing and fragmented communications.
    
    ## The Architecture
    We deployed a custom n8n swarm architecture, integrating their legacy CRM directly with edge-hosted LLMs for real-time processing.
    
    ## The Business Impact
    - **Hours Recovered:** {hours_saved}+ hours per month.
    - **ROI:** {roi_multiplier}x return on automation investment within 60 days.
    """
    return template.strip()

if __name__ == "__main__":
    print(generate_stealth_case_study("FinTech", 450, 3.5))
