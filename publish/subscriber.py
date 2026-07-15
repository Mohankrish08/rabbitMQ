import pika

cred = pika.PlainCredentials(username='mohankrish08', password='Mk@123')

connection = pika.BlockingConnection(pika.ConnectionParameters(host='localhost', port=5672, credentials=cred))
channel = connection.channel()

channel.exchange_declare(exchange='logs', exchange_type='fanout')

result = channel.queue_declare(queue='', exclusive=True)
queue_name = result.method.queue

channel.queue_bind(exchange='logs', queue=queue_name)

def callback(ch, method, properties, body):
    print(f" [X] {body}")

channel.basic_consume(queue=queue_name, on_message_callback=callback)
channel.start_consuming()
