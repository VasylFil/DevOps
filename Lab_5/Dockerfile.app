FROM python:3.8-alpine
LABEL author="V"

RUN apk update \
    && apk upgrade \
    && apk add git \
    && pip install pipenv

WORKDIR /app

COPY my_app/requirements.txt ./
RUN pipenv install -r requirements.txt

COPY my_app/ ./

RUN mkdir logs

EXPOSE 5000

ENTRYPOINT pipenv run python app.py
