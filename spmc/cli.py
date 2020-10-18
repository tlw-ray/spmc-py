import sys
import getopt
import psutil
import consumer
import producer
import queue


process = psutil.Process()


def usage():
    """
    打印使用说明
    :return:
    """

    cpu_list = process.cpu_affinity()
    cpu_list_str = str(cpu_list)
    usage_str = """
[*] 帮助信息:
[*]      使用方式:
[*]          python3 cli.py [选项] 命令
[*]      示例:
[*]          以消费者模式启动: python3 cli.py -c
[*]          以生产者模式启动: python3 cli.py -p
[*]      选项:
[*]          -c --cpu 指定cpu运行, 本机可选值: " + %s
[*]          -q --queue 指定queue的名称, 默认为spmc.queue
[*]          -s --server 指定消息队列主机的名称, 默认为localhost
[*]      命令:
[*]          -p --producer 以生产者的方式运行
[*]          -c --consumer 以消费者的方式运行
[*]          -v --version 打印版本信息
[*]          -h --help 打印帮助信息
[*]          默认: 打印帮助信息
    """ % cpu_list_str
    print(usage_str)


opts, args = getopt.getopt(sys.argv[1:], "q:s:u:hvcp",
                           ['help', 'version', 'queue', 'server', 'cpu', 'consumer', 'producer'])
for op, value in opts:
    if op in ('-u', '--cpu'):
        # 绑定到指定cpu
        process.cpu_affinity([int(value)])
        print("[*] Bind cpu in " + value)

    if op in ('-q', '--queue'):
        queue.name = value

    if op in ('-s', '--server'):
        queue.host = value

    if op in ('-p', '--producer'):
        producer.run()
    elif op in ('-c', '--consumer'):
        consumer.run()
    elif op in ('-v', '--version'):
        print("[*] 单生产者多消费者示例程序")
        print("[*] SPMC")
        print("[*] Version 0.0.1")
        sys.exit()
    elif op in ('-h', '--help'):
        usage()
        sys.exit()