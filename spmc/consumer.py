import pika
import pickle
import queue


def callback(ch, method, properties, body):
    task = pickle.loads(body)
    print("消费: " + str(task) + "\t执行: " + str(task.call()))


def run():
    connection = pika.BlockingConnection(pika.ConnectionParameters(queue.host))
    channel = connection.channel()
    channel.queue_declare(queue=queue.name)
    channel.basic_consume(queue.name, callback, auto_ack=True)
    channel.start_consuming()






