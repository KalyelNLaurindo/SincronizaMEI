#!/bin/bash
# ==============================================================================
# SincronizaMEI - Vault Initializer (Dev Mode)
# ==============================================================================
# Este script deve ser acionado logo apos iniciar o vault dev `docker-compose up -d vault`
# Ele auto-injetar os segredos para a applicacao.

export VAULT_ADDR='http://127.0.0.1:8200'
export VAULT_TOKEN='root'

echo "=========================================="
echo " Conectando ao Vault em $VAULT_ADDR"
echo "=========================================="

# Habilitando motor KV V2 no caminho "secret" se nao houver
vault secrets enable -path=secret -version=2 kv 2>/dev/null || true

# Gerando a chave Random de 32 bytes em Base64
NEW_AES_KEY=$(openssl rand -base64 32)
echo "Generated New AES 256 Key"

# Escrevendo no Vault path `secret/sincronizamei`
vault kv put secret/sincronizamei \
  AES_SECRET_KEY="$NEW_AES_KEY" \
  POSTGRES_PASSWORD="devpassword" \
  REDIS_PASSWORD="devredis" \
  RABBITMQ_PASSWORD="devrabbit"

echo "Secrets injetados e mapeados no cofre para o path 'secret/sincronizamei' com sucesso!"
