def aggregate_contract_metrics(parsed_contracts):
    metrics = {"net_30": 0, "net_60": 0, "auto_renew": 0, "manual_renew": 0}
    total_mrr = 0
    
    for contract in parsed_contracts:
        total_mrr += contract.get("mrr_value", 0)
        
        if contract.get("payment_terms") == "Net 30": metrics["net_30"] += 1
        elif contract.get("payment_terms") == "Net 60": metrics["net_60"] += 1
        
        if contract.get("renewal_type") == "Auto": metrics["auto_renew"] += 1
        else: metrics["manual_renew"] += 1
        
    print("--- B2B Contract Portfolio Health ---")
    print(f"Total Contracted MRR: ${total_mrr:,}")
    print(f"Payment Terms: {metrics['net_30']} on Net 30 | {metrics['net_60']} on Net 60")
    print(f"Renewal Risk: {metrics['manual_renew']} manual renewals require immediate sales follow-up.")
    
    return metrics

if __name__ == "__main__":
    mock_data = [
        {"client": "Alpha", "mrr_value": 15000, "payment_terms": "Net 30", "renewal_type": "Auto"},
        {"client": "Beta", "mrr_value": 8500, "payment_terms": "Net 60", "renewal_type": "Manual"}
    ]
    aggregate_contract_metrics(mock_data)
