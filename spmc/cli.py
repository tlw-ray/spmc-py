import sys
import getopt
import psutil
import consumer
import producer
import queue


process = psutil.Process()


def usage():
    cpu_list = process.cpu_affinity()
    print("[*] 帮助信息:")
    print("[*]      使用方式:")
    print("[*]          python3 cli.py [选项] 命令")
    print("[*]      示例:")
    print("[*]          以消费者模式启动: python3 cli.py -c")
    print("[*]          以生产者模式启动: python3 cli.py -p")
    print("[*]      选项:")
    print("[*]          -c --cpu 指定cpu运行, 本机可选值: " + str(cpu_list))
    print("[*]          -q --queue 指定queue的名称, 默认为spmc.queue")
    print("[*]          -s --server 指定消息队列主机的名称, 默认为localhost")
    print("[*]      命令:")
    print("[*]          -p --producer 以生产者的方式运行")
    print("[*]          -c --consumer 以消费者的方式运行")
    print("[*]          -v --version 打印版本信息")
    print("[*]          -h --help 打印帮助信息")
    print("[*]          默认: 打印帮助信息")


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