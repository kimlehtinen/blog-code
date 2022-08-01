# Flask database migrations using Flask-Migrate

## Install dependencies
```
pip install -r requirements.txt
```

## Run locally
```
python3 app.py
```

## Create migration
```
python3 -m flask db migrate
```

## Apply migrations
```
python3 -m flask db upgrade
```

## Downgrade migrations
```
python3 -m flask db downgrade
```

## Docker
```
docker-compose up --build -d
```
