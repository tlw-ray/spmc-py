import random


class Task:
    """
    各种Task的基类
    """
    def call(self):
        pass


class AddIntTask:
    """
    两个整数相加的Task
    """
    def __init__(self, left, right):
        self.left = left
        self.right = right

    def __str__(self):
        return 'AddIntTask{left: %d, right: %d}' %(self.left, self.right)

    def call(self):
        return self.left + self.right


class PrintStringTask:
    """
    返回'打印: xxx'字符串的Task
    """
    def __init__(self, content):
        self.content = content

    def __str__(self):
        return 'PrintStringTask{content: %s}' %(self.content)

    def call(self):
        return "打印:" + self.content


def create_task():
    """
    根据随机整数是否能被2正处来随机创建两种Task的方法
    :return:
    """
    if random.randint(0, 1) % 2 == 0:
        left = random.randint(0, 100)
        right = random.randint(0, 100)
        return AddIntTask(left, right)
    else:
        content = str(random.random())
        return PrintStringTask(content)

