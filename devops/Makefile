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
