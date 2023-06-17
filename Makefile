
# ------------- Run with UviCorn ------------------------------

.PHONY: run

make run-db: ## setup timescale db
	docker pull timescale/timescaledb:latest-pg14
	docker run -d --name timescaledb --restart=always -p 5432:5432 -e POSTGRES_PASSWORD=your_password -v timescaledb_data:/var/lib/postgresql/data timescale/timescaledb:latest-pg14


activate-pipenv: ##
	pipenv shell



run: ## run App on UviCorn server
	uvicorn app.main:app --host 127.0.0.1 --port 8010 --reload




# ------------  Docker  -----------------------------------

.PHONY: docker-build docker-run docker-clean

DOCKER_IMAGE = fastapi-timescaledb-timeseries-demo

docker-build: ## build docker image from Dockerfile
	docker build -t $(DOCKER_IMAGE) .

docker-run: ## run API docker container
	docker run -p 5000:5000 $(DOCKER_IMAGE)

docker-clean: ## remove docker image
	docker stop $(DOCKER_IMAGE)
	docker rm $(DOCKER_IMAGE)
	docker rmi -f $(DOCKER_IMAGE)





# ------------  Help  --------------------------------------

.PHONY: help

help: ## This help.
	@awk 'BEGIN {FS = ":.*?## "} /^[a-zA-Z_-]+:.*?## / {printf "\033[36m%-30s\033[0m %s\n", $$1, $$2}' $(MAKEFILE_LIST)

.DEFAULT_GOAL := help


