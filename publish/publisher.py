import pika, sys

cred = pika.PlainCredentials(username='mohankrish08', password='Mk@123')

connection = pika.BlockingConnection(pika.ConnectionParameters(host='localhost', port=5672, credentials=cred))
channel = connection.channel()

channel.exchange_declare(exchange='logs', exchange_type='fanout')

message = ' '.join(sys.argv[1:]) or "info: broadcast message"
channel.basic_publish(exchange='logs', routing_key='', body=message)
print(f" [X] Sent {message}")
connection.close()
