def trigger_renewal_negotiation(client_name, contract_expiry_date, hours_saved_ytd):
    print(f"[BizOps] Contract for {client_name} expiring on {contract_expiry_date}. Initiating renewal sequence.")
    
    renewal_pitch = f"""
    Hi {client_name} team,
    
    As we approach your annual renewal, I wanted to share the exact impact of our infrastructure: we've successfully automated {hours_saved_ytd} hours of engineering overhead this year.
    
    To maintain uninterrupted zero-downtime service, you can click here to securely authorize your SLA renewal for 2027.
    """
    
    print("[+] Renewal data compiled. Dispatching secure e-signature portal link.")
    return renewal_pitch

if __name__ == "__main__":
    trigger_renewal_negotiation("Enterprise_Alpha", "2026-08-07", hours_saved_ytd=4250)
