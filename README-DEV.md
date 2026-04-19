# 🚀 Guia de Desenvolvimento Local

Para rodar a infraestrutura local (PostgreSQL, Redis, RabbitMQ e Vault), siga as etapas abaixo:

## 1. Configurar as variáveis de ambiente:
```bash
cp .env.example .env
```
*Não esqueça de preencher as chaves de senha do banco dentro do seu arquivo `.env`!*

## 2. Subir os containers em background:
```bash
docker-compose up -d
```

## 3. Verificando integridade:
Você pode rodar `docker-compose ps` para verificar se todos os containers iniciaram corretamente e contêm o status `(healthy)`.

## Portas Úteis (Ambiente Local)
- **PostgreSQL:** `5432`
- **Redis:** `6379`
- **RabbitMQ (AMQP):** `5672`
- **RabbitMQ (UI):** `15672` (Acesso via navegador web)
- **Vault:** `8200`
