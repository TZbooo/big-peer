FROM python:3.10

ENV PYTHONUNBUFFERED 1

COPY ./requirements.txt /requirements.txt

RUN apt update \
    && apt install -y apache2-utils \
    && pip install -r /requirements.txt

WORKDIR /code
COPY . /code