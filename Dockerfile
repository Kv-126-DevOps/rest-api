FROM python:3.9-slim
WORKDIR /usr/src/app
COPY requirements_old.txt ./
RUN pip3 install --upgrade pip
RUN pip3 install --no-cache-dir -r requirements.txt
COPY . .
CMD  [ "python3", "-m" , "flask", "run", "--host=0.0.0.0"]
