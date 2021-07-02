# RabbitMQ Event bus logger
# python consumer.py in cd admin && docker-compose exec backend sh  
import pika, json, os, django

# Erro Django - customer.py outside of folder
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "admin.settings")
django.setup()

from products.models import Product

params = pika.URLParameters('amqps://xogussja:Rg2fhAoJyQkmQBkot2u9buS5r0f3xkIL@snake.rmq2.cloudamqp.com/xogussja')

connection = pika.BlockingConnection(params)

channel = connection.channel()

channel.queue_declare(queue='admin')

def callback(ch, method, properties, body):
    print('Received in admin')
    id = json.loads(body)
    print(' === ')
    #print(id)
    product = Product.objects.get(id=id)
    product.likes = product.likes + 1
    product.save()
    print('Product likes increased!')

channel.basic_consume(queue='admin', on_message_callback=callback, auto_ack=True)

print('Started start_consuming')

channel.start_consuming()

channel.close()