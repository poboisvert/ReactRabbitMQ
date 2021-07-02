# RabbitMQ Event bus logger
# python consumer.py in cd admin && docker-compose exec backend sh  
import pika, json

from main import Product, db

params = pika.URLParameters('amqps://xogussja:Rg2fhAoJyQkmQBkot2u9buS5r0f3xkIL@snake.rmq2.cloudamqp.com/xogussja')

connection = pika.BlockingConnection(params)

channel = connection.channel()

channel.queue_declare(queue='main')
# channel is main for Flask

def callback(ch, method, properties, body):
    print('Received a call in Main')
    #print(body)
    data = json.loads(body)
    print(data)

    if properties.content_type == 'product_created':
        product = Product(id=data['id'], title=data['title'], description=data['description'], image=data['image'])
        db.session.add(product)
        db.session.commit()
        # Terminal
        print('Product Received & Created')

    elif properties.content_type == 'product_updated':
        product = Product.query.get(data['id'])
        product.title = data['title']
        product.description = data['description']
        product.image = data['image']
        db.session.commit()
        # Terminal
        print('Product Updated')

    elif properties.content_type == 'product_deleted':
        product = Product.query.get(data)
        db.session.delete(product)
        db.session.commit()
        # Terminal
        print('Product Deleted')

channel.basic_consume(queue='main', on_message_callback=callback, auto_ack=True) # channel is main for Flask

print('Started start_consuming')

channel.start_consuming()

channel.close()