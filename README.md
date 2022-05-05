# RestAPI
This is a REST API application that returns an issues filtered by label

## Create infrastructure
	docker network create -d bridge kv126
	docker run --network=kv126 -d --name postgres -e POSTGRES_USER=dbuser -e POSTGRES_PASSWORD=dbpass postgres
	docker run --network=kv126 -d --name rabbit -e RABBITMQ_DEFAULT_USER=mquser -e RABBITMQ_DEFAULT_PASS=mqpass -p 15672:15672 rabbitmq:3.9-management

### Run rabbit-to-bd
	git clone --branch 1-rabbit-to-bd-code-refactoring https://github.com/Kv-126-DevOps/rabbit-to-bd.git /opt/rabbit-to-bd
	docker run --network=kv126 -d --name rabbit-to-bd -e POSTGRES_HOST=$(docker inspect -f '{{range.NetworkSettings.Networks}}{{.IPAddress}}{{end}}' postgres) -e POSTGRES_PORT=5432 -e POSTGRES_USER=dbuser -e POSTGRES_PW=dbpass -e POSTGRES_DB=postgres -e RABBIT_HOST=rabbit -e RABBIT_PORT=5672 -e RABBIT_USER=mquser -e RABBIT_PW=mqpass -e RABBIT_QUEUE=restapi -v /opt/rabbit-to-bd:/app python:3.9-slim sleep infinity
	docker exec rabbit-to-bd pip install -r /app/requirements.txt
	docker exec -d rabbit-to-bd bash -c "cd /app && python ./app.py"

### Run rest-api (port 8080)
	git clone --branch 14-rest-api-code-refactoring https://github.com/Kv-126-DevOps/rest-api.git /opt/rest-api
	docker run --network=kv126  -d --name rest-api -e POSTGRES_HOST=$(docker inspect -f '{{range.NetworkSettings.Networks}}{{.IPAddress}}{{end}}' postgres) -e POSTGRES_PORT=5432 -e POSTGRES_USER=dbuser -e POSTGRES_PASS=dbpass -e POSTGRES_DB=postgres -v /opt/rest-api:/app -p 8080:5000 python:3.9-slim sleep infinity
	docker exec rest-api pip install -r /app/requirements.txt
	docker exec -d rest-api bash -c "cd /app && flask run --host=0.0.0.0"
