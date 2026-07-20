provider "aws" {
  region = "us-east-1"
}

module "eks" {
  source          = "terraform-aws-modules/eks/aws"
  version         = "20.0.0"
  cluster_name    = "b2b-enterprise-pipeline"
  cluster_version = "1.30"
  
  vpc_id          = module.vpc.vpc_id
  subnet_ids      = module.vpc.private_subnets

  eks_managed_node_groups = {
    ai_workers = {
      min_size     = 2
      max_size     = 10
      desired_size = 3
      instance_types = ["t3.xlarge"]
      
      labels = {
        role = "heavy-ai-processing"
      }
    }
  }
}

output "cluster_endpoint" {
  value = module.eks.cluster_endpoint
}
