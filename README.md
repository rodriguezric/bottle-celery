# Bottle & Celery
This is a minimal setup for getting a local Bottle API with Celery for asynchronous tasks.

## Prerequisuites
1. This guide assumes you have docker setup in your environment.
2. This was built using Python 3.8. The requirements.txt was not tested with other versions.

## Installation
1. Clone this repo
2. Make a virtual environment
```shell
python -m venv .venv
. .venv/bin/activate
```
3. Install the requirements
You can either use the frozen requirements text or manually pip-install bottle, celery, and redis.
```shell
python -m pip install requirements.txt
```
4. Run a redis container
```shell
docker container run -d -p 6379:6379 redis
```
Adjust the ports in this command and in the script if 6379 is already used in your environment.

5. Run celery worker
```shell
celery -A main worker
```

6. Run the bottle API
```shell
python main.py
```
