import pika, json

params = pika.URLParameters('amqps://xogussja:Rg2fhAoJyQkmQBkot2u9buS5r0f3xkIL@snake.rmq2.cloudamqp.com/xogussja')

connection = pika.BlockingConnection(params)

channel = connection.channel()

def publish(method, body):
    properties = pika.BasicProperties(method)
    channel.basic_publish(exchange='', routing_key='admin', body=json.dumps(body), properties=properties)