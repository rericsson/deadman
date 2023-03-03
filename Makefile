install:
	pip install --upgrade pip &&\
		pip install -r requirements.txt

lint:
	pylint --disable=R,C app/*.py testing/*.py

format:
	black app/*.py testing/*.py

run:
	flask --app hello run

all: install lint format run 
