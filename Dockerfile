FROM python:3.8.1-slim-buster
WORKDIR /usr/src/app

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# install system dependencies
RUN apt-get update && apt-get install -y netcat iputils-ping curl pipenv

COPY . /usr/src/app/

RUN pip install pipenv && pipenv install --deploy --system