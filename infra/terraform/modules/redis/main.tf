variable "environment" {}
variable "vpc_id" {}
variable "subnet_ids" {}
variable "node_type" {}

resource "aws_elasticache_cluster" "redis" {
  cluster_id           = "sincronizamei-redis-${var.environment}"
  engine               = "redis"
  node_type            = var.node_type
  num_cache_nodes      = 1
  parameter_group_name = "default.redis7"
}

output "endpoint" {
  value = aws_elasticache_cluster.redis.cache_nodes[0].address
}
