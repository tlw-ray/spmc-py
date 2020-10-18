import pika
import pickle
import queue
import task
import queue


def run():
    """
    生产者连接RabbitMQ并生成数据, 达到1000条后关闭连接退出
    """
    connection = pika.BlockingConnection(
        pika.ConnectionParameters(queue.host)
    )

    channel = connection.channel()
    channel.queue_declare(queue=queue.name)

    # 产生1000条数据并发布到消息队列
    for i in range(0, 1000):
        task_instance = task.create_task()
        body = pickle.dumps(task_instance)
        channel.basic_publish(exchange='',
                              routing_key=queue.name,
                              body=body)
        print("生产: " + str(task_instance))

    channel.close()
    connection.close()
