FROM python:3.10-slim-buster

ENV PYTHONUNBUFFERED 1
ENV PATH="/root/.local/bin:${PATH}"
ENV PYTHONPATH='/'

COPY  ./poetry.lock /
COPY  ./pyproject.toml /

RUN apt-get update && apt-get install -y curl \
    && curl -sSL https://install.python-poetry.org | python3 - \
    && poetry config virtualenvs.create false \
    && poetry install --no-dev --no-interaction --no-ansi \
    && apt-get remove curl -y

COPY ./app /app
WORKDIR /app

