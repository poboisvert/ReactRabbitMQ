# Event-Driven Architecture (RabbitMQ)


## ENV
- python3 -m venv env

- source env/bin/activate

> cd admin && docker-compose up 

- pip install -r requirements.txt

- cd admin && python manage.py runserver


### Main

#### Activate Shell

> docker-compose exec backend sh

##### Migration
> python manager.py db --help


### RabbitMQ test

> cd admin && docker-compose exec backend sh

> python consumer.py