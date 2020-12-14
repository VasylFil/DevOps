FROM python:3.8-slim

LABEL author='V'
LABEL version=19.03

RUN apt-get update && apt-get upgrade -y

RUN apt-get install git -y && pip install pipenv

WORKDIR /init

RUN git clone https://github.com/vasylfil/lbs.git

WORKDIR /app
RUN cp -r ../init/lbs/Lab_3/* .

RUN pipenv install

EXPOSE 8000

ENTRYPOINT ["pipenv", "run", "python", "manage.py", "runserver", "0.0.0.0:8000"]