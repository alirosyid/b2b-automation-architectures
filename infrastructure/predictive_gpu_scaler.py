import boto3

def request_spot_gpu_instances(instance_type="p3.2xlarge", max_price="3.00", count=2):
    ec2 = boto3.client('ec2')
    
    response = ec2.request_spot_instances(
        SpotPrice=max_price,
        InstanceCount=count,
        Type='one-time',
        LaunchSpecification={
            'ImageId': 'ami-0abcdef1234567890', # Custom ML AMI
            'InstanceType': instance_type,
            'SecurityGroupIds': ['sg-0123456789abcdef0']
        }
    )
    
    request_ids = [req['SpotInstanceRequestId'] for req in response['SpotInstanceRequests']]
    print(f"Requested {count} spot instances. Request IDs: {request_ids}")
    return request_ids
