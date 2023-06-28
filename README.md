# Flask init app

 Flask init app


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
