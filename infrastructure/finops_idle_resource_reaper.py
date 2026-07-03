import boto3
import requests

def scan_and_reap_idle_resources(slack_webhook_url):
    """Identifies unattached EBS volumes and requests Slack approval for deletion."""
    ec2 = boto3.client('ec2', region_name='us-east-1')
    volumes = ec2.describe_volumes(Filters=[{'Name': 'status', 'Values': ['available']}])
    
    idle_vols = []
    total_wasted_cost = 0.0
    
    for vol in volumes['Volumes']:
        idle_vols.append(vol['VolumeId'])
        total_wasted_cost += vol['Size'] * 0.08 # Approx $0.08 per GB/month
        
    if idle_vols:
        msg = f"⚠️ FinOps Alert: Found {len(idle_vols)} idle EBS volumes costing ~$ {total_wasted_cost}/mo. \nVolumes: {idle_vols}\nShould I terminate them?"
        # Send interactive Slack block with "Approve Deletion" button
        payload = {"text": msg}
        requests.post(slack_webhook_url, json=payload)
        print("FinOps alert dispatched to Slack.")
    else:
        print("Infrastructure is optimized. No idle resources found.")

if __name__ == "__main__":
    scan_and_reap_idle_resources("https://hooks.slack.com/services/YOUR/WEBHOOK/URL")
