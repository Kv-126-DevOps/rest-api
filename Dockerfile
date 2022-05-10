FROM python:3.9-slim
RUN groupadd --gid 2000 docker-user && useradd --uid 2000 --gid docker-user --shell /bin/bash --create-home docker-user
USER docker-user
WORKDIR /home/docker-user/app
CMD ["flask", "run", "--host=0.0.0.0"]
