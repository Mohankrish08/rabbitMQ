import pika, sys

cred = pika.PlainCredentials(username='mohankrish08', password='Mk@123')

connection = pika.BlockingConnection(pika.ConnectionParameters(host='localhost', port=5672, credentials=cred))

channel = connection.channel()

channel.queue_declare(queue='task_queue', durable=True)

message = ' '.join(sys.argv[1:]) or 'Hello world!'

channel.basic_publish(
    exchange='',
    routing_key='task_queue',
    body=message,
    properties=pika.BasicProperties(delivery_mode=1)
)
print(f" [X] Sent {message}")
connection.close()

