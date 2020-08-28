FROM python:3.8.5-slim-buster

COPY requirements.txt /ghibli_app/requirements.txt

WORKDIR /ghibli_app

ENV PYTHONPATH .

RUN pip install -r requirements.txt

COPY . /ghibli_app
