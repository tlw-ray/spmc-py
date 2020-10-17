import random


class Task:
    def call(self):
        pass


class AddIntTask:

    def __init__(self, left, right):
        self.left = left
        self.right = right

    def __str__(self):
        return 'AddIntTask{left: %d, right: %d}' %(self.left, self.right)

    def call(self):
        return self.left + self.right


class PrintStringTask:

    def __init__(self, content):
        self.content = content

    def __str__(self):
        return 'PrintStringTask{content: %s}' %(self.content)

    def call(self):
        return "打印:" + self.content


def create_task():
    if random.randint(0, 1) % 2 == 0:
        left = random.randint(0, 100)
        right = random.randint(0, 100)
        return AddIntTask(left, right)
    else:
        content = str(random.random())
        return PrintStringTask(content)

