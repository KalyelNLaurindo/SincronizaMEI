output "db_endpoint" {
  value = module.db.endpoint
}

output "redis_endpoint" {
  value = module.redis.endpoint
}

output "rabbitmq_endpoint" {
  value = module.rabbitmq.endpoint
}

output "lb_dns_name" {
  value = module.lb.dns_name
}
