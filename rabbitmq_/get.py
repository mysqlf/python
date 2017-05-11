#import os
import pika
conn = None


# def callback(ch, method, properties, body):
#     """
#         out body
#     """
#     print(" [x] Recived ch {0}".format(ch))
#     print(" [x] Recived method {0}".format(method))
#     print(" [x] Recived properties {0}".format(properties))
#     print(" [x] Recived %r" % (body, ))

# try:
#     # get connection
#     connection = pika.BlockingConnection(pika.URLParameters('amqp://test:pystudy@121.42.184.241:5672/test'))
#     # get channel
#     channel = connection.channel()
#     # declare queue, 重复声明不会报错，但是没有队列的话直接取用会报错
#     channel.queue_declare(queue='py', durable=True)
#     # get message
#     channel.basic_consume(callback, queue='py', no_ack=True)
#     print(' [*] Waiting for messages. To exit press CTRL+C')
#     channel.start_consuming()
# except Exception as e:
#     raise e
# finally:
#     if conn:
#         conn.close()


# amqp://test:pystudy@121.42.184.241:5672/test

# amqp类
class Amqp():
    # 创建连接

    def __init__(self, host, queue):
        self.connection = pika.BlockingConnection(pika.URLParameters(host))
        # 连接实例
        self.channel = self.connection.channel()
        # 创建队列
        self.channel.queue_declare(queue=queue, durable=True)  # queue='py'

     # 发送消息
    def send(self, ex, route, body):
        self.channel.basic_publish(exchange=ex,
                                   routing_key=route,
                                   body=body)
        # exchange='pystudy',
        # routing_key='pyroute',
        # body='Hello World!'
    # 读取消息

    def get(self, queue):
        self.channel.basic_consume(self.callback, queue=queue, no_ack=True)
        self.channel.start_consuming()
        self.close()
    # 解析消息

    def callback(self, ch, method, properties, body):
        """
            out body
        """
        # print(" [x] Recived ch {0}".format(ch))
        # print(" [x] Recived method {0}".format(method))
        # print(" [x] Recived properties {0}".format(properties))
        print(" [x] Recived %r" % (body, ))

    def close(self):
        if self.connection:
            self.connection.close()
host = 'amqp://test:pystudy@121.42.184.241:5672/test'
queue = 'py'
amqp = Amqp(host, queue)
amqp.send('pystudy', 'pyroute', 'Hello World!')
amqp.get('py')
