# Created by Asher on 2023/5/9
# 默认目标
.DEFAULT_GOAL := help

help: ## Display the help message
	@awk 'BEGIN {FS = ":.*?## "} /^[a-zA-Z_-]+:.*?## / {printf "\033[36m%-15s\033[0m %s\n", $$1, $$2}' $(MAKEFILE_LIST)

frontend: ## Start frontend server 
	@echo "Starting frontend server"
	@cd ./devops && docker-compose up frontend

backend: ## Start backend server 
	@echo "Starting backend server"
	@cd ./devops && docker-compose up backend

