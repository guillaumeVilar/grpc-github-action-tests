.PHONY: stop
stop: ## Stop the docker containers
	docker-compose down

.PHONY: start
start: ## start the docker containers
	docker-compose up -d

.PHONY: restart
restart: stop start## restart the docker containers


.PHONY: rm
rm: ## rm the docker images
	docker image rm grpc-github-action-tests_python-container-1
	docker image rm grpc-github-action-tests_python-container-2

.PHONY: bash1
bash1: ## bash to server container
	docker container exec -it python-container-1 bash

.PHONY: bash2
bash2: ## bash to client container
	docker container exec -it python-container-2 bash

.PHONY: client
client: ## make client request
	docker container exec python-container-2 python /opt/python/execute_script/client.py

.PHONY: server
server: ## make server request
	docker container exec python-container-1 python /opt/python/execute_script/server.py