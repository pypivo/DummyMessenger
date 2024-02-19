FROM python:3.11-buster


WORKDIR /backend

COPY . .

RUN apt-get update && apt install -y python3-dev
RUN pip install --upgrade pip
RUN pip install -r requirements.txt

EXPOSE 8080