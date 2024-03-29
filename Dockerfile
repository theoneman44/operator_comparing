FROM python:3.10.6-alpine

WORKDIR /app

RUN apk update && apk add --no-cache --virtual bash git gcc g++

RUN python -m pip install --upgrade pip

COPY requirements.txt /app/

RUN python -m pip install -r requirements.txt

COPY . /app

CMD ["export FLASK_APP=webapp && export FLASK_ENV=development && flask run"]
