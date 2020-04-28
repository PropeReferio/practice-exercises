#!/usr/bin/env python

import pika

connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
channel = connection.channel()

channel.queue_declare(queue='hello2')

channel.basic_publish(exchange='',
                      routing_key='hello2',
                      body='Hello World!')
print(' [x] Sent "Hello World!"')

connection.close()