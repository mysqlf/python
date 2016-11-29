import os
import pika
conn = None


def callback(ch, method, properties, body):
    """
        out body
    """
    print(" [x] Recived ch {0}".format(ch))
    print(" [x] Recived method {0}".format(method))
    print(" [x] Recived properties {0}".format(properties))
    print(" [x] Recived %r" % (body, ))
try:
    # get connection
    connection = pika.BlockingConnection(pika.URLParameters('amqp://test:pystudy@121.42.184.241:5672/test'))
    # get channel
    channel = connection.channel()
    # declare queue, 重复声明不会报错，但是没有队列的话直接取用会报错
    channel.queue_declare(queue='py', durable=True)
    # get message
    channel.basic_consume(callback, queue='py', no_ack=True)
    print(' [*] Waiting for messages. To exit press CTRL+C')
    channel.start_consuming()
except Exception as e:
    raise e
finally:
    if conn:
        conn.close()
