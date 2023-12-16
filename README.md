# Simple web To-do List

## Run

### Run with venv
```
python -m venv venv
source ./venv/bin/active
pip install -r requirements.txt
python manage.py migrate
python manage.py runserver
```
### Run with docker
```
sudo docker compose run web python manage.py migrate
docker compose up
```
##
### http://localhost:8000