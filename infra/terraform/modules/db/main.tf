variable "environment" {}
variable "vpc_id" {}
variable "subnet_ids" {}
variable "instance_class" {}

resource "aws_db_instance" "postgres" {
  allocated_storage    = 20
  engine               = "postgres"
  engine_version       = "16"
  instance_class       = var.instance_class
  skip_final_snapshot  = true
  identifier           = "sincronizamei-db-${var.environment}"
}

output "endpoint" {
  value = aws_db_instance.postgres.endpoint
}
