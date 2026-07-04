def generate_least_privilege_policy(terraform_state_summary):
    print("[SecOps] Analyzing infrastructure state to generate zero-trust IAM policies...")
    
    # Mock LLM generation based on infrastructure needs
    iam_policy = {
        "Version": "2012-10-17",
        "Statement": [{
            "Effect": "Allow",
            "Action": ["s3:GetObject", "s3:PutObject"],
            "Resource": "arn:aws:s3:::b2b-automation-assets/*"
        }]
    }
    
    print("[+] Least-privilege IAM policy generated. Ready for Terraform injection.")
    return iam_policy

if __name__ == "__main__":
    tf_state = {"resources": ["aws_s3_bucket.b2b-automation-assets"]}
    print(generate_least_privilege_policy(tf_state))
