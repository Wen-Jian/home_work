# FROM python:3.7-slim as base
FROM python:3.7

# Setup env
ENV LANG C.UTF-8
ENV LC_ALL C.UTF-8
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONFAULTHANDLER 1

RUN apt-get update && apt-get install -y --no-install-recommends gcc
RUN apt update && apt install -y libsm6 libxext6
RUN apt-get install -y libxrender-dev
RUN pip install pipenv

COPY . .
RUN pipenv install
CMD pipenv run python manage.py