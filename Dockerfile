FROM python:3.12-slim as builder

RUN apt-get update -yy && apt-get install -yy build-essential

RUN pip install --upgrade pip && \
    pip install poetry

WORKDIR /code
ADD . /code

RUN poetry install
