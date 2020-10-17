import pika
import pickle
import queue
import task

connection = pika.BlockingConnection(
    pika.ConnectionParameters(queue.host)
)


channel = connection.channel()
channel.queue_declare(queue=queue.name)

for i in range(0, 1000):
    task_instance = task.create_task()
    body = pickle.dumps(task_instance)
    channel.basic_publish(exchange='',
                          routing_key=queue.name,
                          body=body)
    print("生产: " + str(task_instance))

channel.close()
connection.close()
