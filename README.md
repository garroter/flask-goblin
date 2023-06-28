# Flask init app + Docker + celery

 Flask init app + Docker + celery


## Install

### Install - packages

```
pip install -r config/requirements.txt
```

### Install - test

- local
```
export FLASK_CONFIG=Dev
python run.py
```
- docker
```
export FLASK_CONFIG=Dev
sudo -E docker-compose  up --build
```

### Install - prod

- local
```
export FLASK_CONFIG=Prod
python run.py
```
- docker
```
export FLASK_CONFIG=Prod
sudo -E docker-compose  up --build
```
## test

```
python -m pytest -vv
```

# Celery - queue

```
celery -A modules.queue.celery:celery worker  -Q queue-test --loglevel=INFO --without-heartbeat=True --without-gossip=True --without-mingle=True
```