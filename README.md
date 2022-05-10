# REST-API

## Overview

This is a REST API application that returns an issues filtered by label

## Prerequisites

* Python 3.8+
* PIP package manager
* Database for data storage
* Docker Engine 20.10+

## Create infrastructure

1. Create docker network

    ```bash
	docker network create -d bridge kv126
    ```

2. Run Postgres Database container with "kv126" network

    ```bash
    docker run --network=kv126 -d --name postgres -e POSTGRES_USER=dbuser -e POSTGRES_PASSWORD=dbpass postgres
    ```

3. Run RabbitMQ container with "kv126" network

    ```bash
	docker run --network=kv126 -d --name rabbit -e RABBITMQ_DEFAULT_USER=mquser -e RABBITMQ_DEFAULT_PASS=mqpass -p 15672:15672 rabbitmq:3.9-management
    ```

## Running the Rabbit-to-db service

1. Clone the repository and go to the application folder

    ```bash
    git clone --branch 1-rabbit-to-bd-code-refactoring https://github.com/Kv-126-DevOps/rabbit-to-db.git /opt/rabbit-to-db
    ```

2. Run Rabbit-to-db container with "kv126" network

    ```bash
	docker run --network=kv126 -d --name rabbit-to-db -e POSTGRES_HOST=$(docker inspect -f '{{range.NetworkSettings.Networks}}{{.IPAddress}}{{end}}' postgres) -e POSTGRES_PORT=5432 -e POSTGRES_USER=dbuser -e POSTGRES_PW=dbpass -e POSTGRES_DB=postgres -e RABBIT_HOST=$(docker inspect -f '{{range.NetworkSettings.Networks}}{{.IPAddress}}{{end}}' rabbit) -e RABBIT_PORT=5672 -e RABBIT_USER=mquser -e RABBIT_PW=mqpass -e RABBIT_QUEUE=restapi -v /opt/rabbit-to-db:/app python:3.9-slim sleep infinity
    ```

3. Install all required python packages

    ```bash
	docker exec rabbit-to-db pip install -r /app/requirements.txt
    ```

4. Run the application

    ```bash
	docker exec -d rabbit-to-db bash -c "cd /app && python ./app.py"
    ```

## Running the REST-API service

1. Clone the repository and go to the application folder

   ```bash
   git clone --branch 14-rest-api-code-refactoring https://github.com/Kv-126-DevOps/rest-api.git /opt/rest-api
   ```

2. Run REST-APi container with "kv126" network

    ```bash
    docker run --network=kv126  -d --name rest-api -e POSTGRES_HOST=$(docker inspect -f '{{range.NetworkSettings.Networks}}{{.IPAddress}}{{end}}' postgres) -e POSTGRES_PORT=5432 -e POSTGRES_USER=dbuser -e POSTGRES_PASS=dbpass -e POSTGRES_DB=postgres -v /opt/rest-api:/home/docker-user/app -p 8080:5000 python:3.9-slim sleep infinity
    ```

3. Install all required python packages

   ```bash
   docker exec rest-api pip install -r /home/docker-user/app/requirements.txt
   ```
4. Run the application

   ```bash
   docker exec -d rest-api bash -c "cd /app && flask run --host=0.0.0.0"
   ```

### REST-API Application Properties

Parameters are set as environment variables

| Parameter     | Default          | Description         |
|:--------------|:-----------------|:--------------------|
| POSTGRES_HOST | None             | PostgreSQL host     |
| POSTGRES_PORT | 5432             | PostgreSQL port     |
| POSTGRES_USER | None             | PostgreSQL user     |
| POSTGRES_PASS | None             | PostgreSQL password |
| POSTGRES_DB   | postgres         | PostgreSQL database |

## Testing

1. Do tests

   ```bash
   curl http://127.0.0.1:8080/Hello-Kv-126-DevOps/
   curl http://127.0.0.1:8080/issues/
   ```
