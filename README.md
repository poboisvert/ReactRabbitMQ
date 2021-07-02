# Event-Driven Architecture (RabbitMQ)

## Architecture

![Diagram](Diagram.drawio.svg)

## Flow & Events
- Admin Service (Product Service): Use by the front end to aggregate the product informations
    - Events:
        - product_created
        - product_updated
        - product_deleted

![preview](admin_service.png)

- Main Service (Like Service): Use by the front end to aggregate likes and increment
    - Event:
        - product_liked

![preview](main_service.png)

- Frontend: Connect to both backend 8000 & 8005


## ENV
> python3 -m venv env

> source env/bin/activate

> cd admin && docker-compose up 

> pip install -r requirements.txt

> cd admin && python manage.py runserver


### Main

#### Activate Shell

> docker-compose exec backend sh

##### Migration
> python manager.py db --help


### RabbitMQ test

> cd admin && docker-compose exec backend sh

> python consumer.py

### Referencies
- https://www-freecodecamp-org.cdn.ampproject.org/v/s/www.freecodecamp.org/news/python-microservices-course/amp/?amp_js_v=a6&amp_gsa=1&usqp=mq331AQFKAGwASA%3D#csi=0&referrer=https%3A%2F%2Fwww.google.com&amp_tf=Fonte%3A%20%251%24s&ampshare=https%3A%2F%2Fwww.freecodecamp.org%2Fnews%2Fpython-microservices-course%2F

- https://youtu.be/0iB5IPoTDts