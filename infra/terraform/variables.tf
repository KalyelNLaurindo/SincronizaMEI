variable "aws_region" {
  type    = string
  default = "sa-east-1"
}

variable "environment" {
  type = string
}

variable "vpc_cidr" {
  type = string
}

variable "db_instance_class" {
  type = string
}

variable "redis_node_type" {
  type = string
}

variable "rabbitmq_instance_type" {
  type = string
}
