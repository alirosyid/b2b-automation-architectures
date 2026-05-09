# Terraform configuration for deploying the Automation Architecture

terraform {
  required_providers {
    aws = {
      source  = "hashicorp/aws"
      version = "~> 5.0"
    }
  }
}

provider "aws" {
  region = "us-east-1"
}

# ECS Cluster for Python Microservices
resource "aws_ecs_cluster" "automation_cluster" {
  name = "b2b-automation-microservices"
}

# Placeholder for n8n EC2 Instance
resource "aws_instance" "n8n_server" {
  ami           = "ami-0c55b159cbfafe1f0" # Ubuntu Server 22.04 LTS
  instance_type = "t3.medium"
  tags = {
    Name = "n8n-orchestrator-node"
  }
}
