.PHONY: stop
stop: ## Stop the docker containers
	docker-compose down
	docker container stop python-container-1
	docker container rm python-container-1
	docker container stop python-container-2
	docker container rm python-container-2

.PHONY: rm
rm: ## rm the docker images
	docker image rm grpc-github-action-tests_python-container-1
	docker image rm grpc-github-action-tests_python-container-2

.PHONY: start
start: ## start the docker containers
	docker-compose up

.PHONY: bash1
bash1: ## bash to server container
	docker container exec -it python-container-1 bash

.PHONY: bash2
bash2: ## bash to server container
	docker container exec -it python-container-2 bash

.PHONY: client
client: ## make client request
	docker container exec python-container-2 python /opt/python/greeter_client.py