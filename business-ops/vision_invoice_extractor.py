def extract_invoice_data(image_path):
    print(f"[*] Processing visual invoice data from: {image_path}")
    
    # Simulating a call to a Vision API passing the base64 image
    mock_api_response = {
        "vendor": "CloudHost LLC",
        "total_amount": 1450.00,
        "due_date": "2026-07-15",
        "line_items": ["Compute: $1000", "Bandwidth: $450"]
    }
    
    print(f"[+] Extraction successful: {mock_api_response['vendor']} - ${mock_api_response['total_amount']}")
    return mock_api_response

if __name__ == "__main__":
    extract_invoice_data("./inbound_invoices/july_cloud_bill.png")
