import pika
import time

connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
channel = connection.channel()

channel.exchange_declare(exchange='logs', exchange_type='fanout') #durable means that even 

result = channel.queue_declare(queue='', exclusive=True) #Giving queue param
#an empty string results in a randomly generated queue name 
# exclusive deletes it after connection is closed

queue_name = result.method.queue
channel.queue_bind(exchange='logs', #binds to our queue
                   queue=queue_name) 

print(' [*] Waiting for messages. To exit press CTRL+C')

def callback(ch, method, properties, body):
    print(" [x] Received %r" % body)


channel.basic_consume(queue=queue_name,
                      on_message_callback=callback,
                      auto_ack=True)

channel.start_consuming()