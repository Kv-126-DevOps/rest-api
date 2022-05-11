FROM python:3.9-slim
RUN groupadd -g 999 app-user && useradd -r -u 999 -g app-user app-user
USER app-user
WORKDIR /home/app-user/app
RUN pip3 install -r /home/app-user/app/requirements.txt
CMD [ "python3", "-m", "flask", "run", "--host=0.0.0.0"]
