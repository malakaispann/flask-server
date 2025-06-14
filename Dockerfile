FROM python:3.12-slim

RUN apt-get update && \
    apt-get upgrade --assume-yes && \
    apt-get install --assume-yes \
    bash \
    curl

COPY requirements.txt /tmp

RUN python3 -m pip install --requirement /tmp/requirements.txt
