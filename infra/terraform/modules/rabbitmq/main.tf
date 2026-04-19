variable "environment" {}
variable "vpc_id" {}
variable "subnet_ids" {}
variable "instance_type" {}

resource "aws_mq_broker" "rabbitmq" {
  broker_name = "sincronizamei-rmq-${var.environment}"
  engine_type = "RabbitMQ"
  engine_version = "3.13"
  host_instance_type = var.instance_type
  security_groups = []
  
  user {
    username = "admin"
    password = "change_me_in_vault"
  }
}

output "endpoint" {
  value = aws_mq_broker.rabbitmq.instances[0].endpoint
}
