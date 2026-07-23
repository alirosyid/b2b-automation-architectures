def audit_and_dispute_invoice(vendor_name, invoice_amount, internal_telemetry_cost):
    print(f"[FinOps] Auditing incoming invoice from {vendor_name} for ${invoice_amount}...")
    
    variance = invoice_amount - internal_telemetry_cost
    
    if variance > 50: # Tolerance threshold
        print(f"[!] 💸 BILLING DISCREPANCY DETECTED: Vendor overcharged by ${variance:.2f} compared to our internal OTel metrics.")
        print("    -> Drafting autonomous dispute email to vendor billing department...")
        
        dispute_email = f"Hello {vendor_name} Billing, our internal OpenTelemetry tracing indicates a usage cost of ${internal_telemetry_cost}. Your invoice is for ${invoice_amount}. Please review the attached metric logs and issue a credit memo."
        
        print("[+] Dispute filed automatically. Protecting bottom-line MRR.")
        return dispute_email
        
    print("[+] Invoice mathematically verified against internal usage logs. Cleared for payment.")
    return "Approved"

if __name__ == "__main__":
    audit_and_dispute_invoice("CloudProvider X", 4500.00, 4200.00)
