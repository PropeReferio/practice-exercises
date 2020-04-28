#!/usr/bin/env python
import pika
import sys

connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
channel = connection.channel()

channel.exchange_declare(exchange='logs', #This sends messages to the logs
                         exchange_type='fanout') # exchange, which then sends
                #messages to all the queues it knows.

message = ' '.join(sys.argv[1:]) or "info: Hello World!"
channel.basic_publish(exchange='logs', #Name of exchange goes here
                      routing_key='', 
                      body=message)

print(" [x] Sent %r" % message)

connection.close()