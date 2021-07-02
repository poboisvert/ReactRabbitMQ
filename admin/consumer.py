# RabbitMQ Event bus logger
# python consumer.py in cd admin && docker-compose exec backend sh  
import pika

params = pika.URLParameters('amqps://xogussja:Rg2fhAoJyQkmQBkot2u9buS5r0f3xkIL@snake.rmq2.cloudamqp.com/xogussja')

connection = pika.BlockingConnection(params)

channel = connection.channel()

channel.queue_declare(queue='admin')

def callback(ch, method, properties, body):
    print('Received a call in Admin')
    print(body)

channel.basic_consume(queue='admin', on_message_callback=callback, auto_ack=True)

print('Started start_consuming')

channel.start_consuming()

channel.close()