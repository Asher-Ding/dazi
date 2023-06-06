# Created by Asher on 2023/5/9
# 默认目标
.DEFAULT_GOAL := help

help: ## Display the help message
	@awk 'BEGIN {FS = ":.*?## "} /^[a-zA-Z_-]+:.*?## / {printf "\033[36m%-15s\033[0m %s\n", $$1, $$2}' $(MAKEFILE_LIST)

run_frontend: ## Start frontend server 
	@echo "Starting frontend server"
	@docker-compose up frontend

run_backend: ## Start backend server 
	@echo "Starting backend server"
	@docker-compose up backend

run_db: ## Start database server 
	@echo "Starting database server"
	@docker-compose up db mongo-express

run_vault: ## Start vault server 
	@echo "Starting vault server"
	@docker-compose up vault

create_secret: ## Create secret in vault；创建vault中的secret；可能需要执行docker swarm init; If the secret already exists, you may have to delete it first by running: docker secret rm <secret_name>
	@echo "Creating secret from vault; We will creat secrets, and output the secret ids"
	@echo '{"Name": "db_username", "Driver": "vault", "DriverOpts": {"vault-path": "secret/dazi/db", "vault-field": "secret.db_username"}}' | docker secret create db_username -
	@echo '{"Name": "db_password", "Driver": "vault", "DriverOpts": {"vault-path": "secret/dazi/db", "vault-field": "secret.db_password"}}' | docker secret create db_password -

delete_secret: ## Delete secret in vault；删除vault中的secret；可能需要执行docker swarm init
	@echo "Deleting secret from vault; We will delete secrets"
	@docker secret rm db_username
	@docker secret rm db_password
	