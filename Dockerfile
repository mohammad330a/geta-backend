FROM python:3.9.6

RUN mkdir /code
WORKDIR /code

RUN apt-get update -y

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

RUN pip install --upgrade pip
COPY requirements /code/
RUN pip install -r requirements

COPY . /code/
