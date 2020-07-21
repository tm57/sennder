FROM python:3.8.1-slim-buster
WORKDIR /usr/src/app

# set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# install system dependencies
RUN apt-get update && apt-get install -y netcat iputils-ping curl pipenv

# install dependencies
RUN pip install --upgrade pip
RUN pipenv install django
# copy project
COPY . /usr/src/app/

EXPOSE 3000

CMD ["python", "manage.py runserver"]