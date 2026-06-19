def scan_contract_terms(contract_text, risk_parameters):
    flagged_clauses = []
    
    for term in risk_parameters:
        if term.lower() in contract_text.lower():
            flagged_clauses.append(term)
            print(f"[Legal Ops] 🚩 DANGER: Unacceptable clause detected -> '{term}'")
            
    if not flagged_clauses:
        return "Contract approved for final human review."
        
    return f"Contract rejected. Redlined items: {flagged_clauses}"

if __name__ == "__main__":
    sample_nda = "The receiving party assumes unlimited liability for all data breaches."
    unacceptable_terms = ["unlimited liability", "perpetual exclusivity", "net 90"]
    print(scan_contract_terms(sample_nda, unacceptable_terms))
