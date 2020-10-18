import pika
import pickle
import queue


def callback(ch, method, properties, body):
    """
    接收到消息后执行回调, 输出消费的内容和执行的结果
    :param ch: 消息队列的channel
    :param method: pika.spec.Basic.Deliver
    :param properties:pika.spec.BasicProperties
    :param body: 消息的二进制内容
    :return:
    """
    task = pickle.loads(body)
    print("消费: " + str(task) + "\t执行: " + str(task.call()))


def run():
    """
    消费者, 连接RabbitMQ, 尝试声明队列, 监听并等待
    """
    connection = pika.BlockingConnection(pika.ConnectionParameters(queue.host))
    channel = connection.channel()
    channel.queue_declare(queue=queue.name)
    channel.basic_consume(queue.name, callback, auto_ack=True)
    channel.start_consuming()

