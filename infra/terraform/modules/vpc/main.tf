variable "environment" {}
variable "vpc_cidr" {}

resource "aws_vpc" "main" {
  cidr_block = var.vpc_cidr
  tags = {
    Name = "sincronizamei-vpc-${var.environment}"
  }
}

output "vpc_id" {
  value = aws_vpc.main.id
}

output "private_subnets" {
  value = ["subnet-mock-private-1", "subnet-mock-private-2"]
}

output "public_subnets" {
  value = ["subnet-mock-public-1", "subnet-mock-public-2"]
}
