#!/usr/bin/env python
import pika

connection = pika.BlockingConnection(pika.URLParameters('amqp://test:pystudy@121.42.184.241:5672/test'))
channel = connection.channel()
channel.queue_declare(queue='py', durable=True)
channel.basic_publish(exchange='pystudy',
                      routing_key='pyroute',
                      body='Hello World!')

#print(" [x] Sent 'Hello World!'")
connection.close()
