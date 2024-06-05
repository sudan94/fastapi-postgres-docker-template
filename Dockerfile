FROM python:3.9-slim

WORKDIR /app

COPY requirements.txt .

RUN apt-get update \
    && apt-get install gcc -y \
    && apt-get clean

RUN pip install -r ./requirements.txt \
    && rm -rf /root/.cache/pip

COPY . .