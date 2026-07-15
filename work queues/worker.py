import pika, time

cred = pika.PlainCredentials(username='mohankrish08', password='Mk@123')

connection = pika.BlockingConnection(pika.ConnectionParameters(host='localhost', port=5672, credentials=cred))
channel = connection.channel()

channel.queue_declare(queue='task_queue', durable=True)

def callback(ch, method, properties, body):
    print(f" [X] Received {body.decode()}")
    time.sleep(body.count(b'.'))
    print(" [X] Done")
    ch.basic_ack(delivery_tag = method.delivery_tag)

channel.basic_qos(prefetch_count=2)
channel.basic_consume(queue='task_queue', on_message_callback=callback)

print(' [*] Waiting for messages.')
channel.start_consuming()