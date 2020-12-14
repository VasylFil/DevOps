.DEFAULT_GOAL := all

all: install test run deploy

install:
	echo "Installing pipenv and dependencies..."
	pip3 install pipenv
	pipenv --python 3.8
	pipenv install requests
	pipenv install ntplib
	pipenv install pytest

test:
	echo "Starting tests..."
	echo "_______TEST: `date`_______" >> results.txt
	pipenv run pytest tests/tests.py >> results.txt

run:
	echo "Run Python app."
	echo "_______RUN: `date`_______" >> results.txt
	pipenv run python3 app.py >> results.txt

deploy:
	echo "Adding and Committing results.txt to git."
	git add results.txt
	git commit -m "Lab_2: DEPLOY: `date`"
	git push origin main Lab_2
	echo "Bomb has been planted ☺"
