import boto3
import json
from datetime import datetime

def collect_iam_evidence():
    """Collects IAM credential reports for SOC2 compliance evidence."""
    client = boto3.client('iam')
    response = client.generate_credential_report()
    
    if response['State'] == 'COMPLETE':
        report = client.get_credential_report()
        csv_content = report['Content'].decode('utf-8')
        
        filename = f"soc2_iam_report_{datetime.now().strftime('%Y_%m')}.csv"
        with open(f"/secure_vault/compliance/{filename}", "w") as f:
            f.write(csv_content)
        print(f"SOC2 Evidence saved: {filename}")
    else:
        print("Report generation in progress. Retry triggered.")

if __name__ == "__main__":
    collect_iam_evidence()
