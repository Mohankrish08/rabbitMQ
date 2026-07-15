# importing libraries
import pika 

cred = pika.PlainCredentials(username='mohankrish08', password='Mk@123')

connection = pika.BlockingConnection(pika.ConnectionParameters(host='localhost', port=5672, credentials=cred))
channel = connection.channel()

channel.queue_declare(queue='hello')

def callback(ch, method, properties, body):
    print(f"[X] Received {body}")

channel.basic_consume(queue='hello', on_message_callback=callback, auto_ack=True)

print(' [*] Waiting for messages. To exit press CTRL+C')
channel.start_consuming()