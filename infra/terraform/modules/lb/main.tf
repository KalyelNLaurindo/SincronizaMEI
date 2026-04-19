variable "environment" {}
variable "vpc_id" {}
variable "public_subnets" {}

resource "aws_lb" "main" {
  name               = "sincronizamei-lb-${var.environment}"
  internal           = false
  load_balancer_type = "application"
}

output "dns_name" {
  value = aws_lb.main.dns_name
}
