FROM python:3.7-slim

ENV API_KEY 1234567890

COPY ./src /code
WORKDIR /code

RUN apt-get update && \
    apt-get install -y wget nano && \
    rm -rf /var/lib/apt/lists/* && \
    pip3 install -r requirements.txt

CMD python3 -u main.py
