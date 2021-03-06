# 单生产者多消费者python版本程序

## 需求

1. 一个生产者，多个消费者，消费者用多进程处理任务， 生产者连续地随机生成任务放入消息队列( 如打印字符串任务、整数加法任务)。程序能充分利用CPU计算的资源，每个任务只在一个CPU核心上运行。
2. 生产者需要记录已经完成的任务的数量，如果当前已完成的任务数量超过1000，那么停止生产。
3. 生产者和消费者之间使用消息队列通信，消息队列是进程安全的。
4. 如果消息队列为空，消费者进程能阻塞等待；
5. 使用多态来支持不同种类的任务需求。
6. 一个完整的程序，包括指明所使用的库（#include/ import等），和相应的程序入口main 函数。
7. 代码不需要编译运行，尽量保持语法正确。可以上网搜索资料，但不能连续copy超过1行的代码。

## 分析

1. 一生产者多消费者: 
    - 不需要考虑消息顺序问题
    - 多消费者假设是对等的, 认为是随机消费任务的
    - 如果已经存在消费者存在, 不能再创建新的消费者
2. 消费者用多进程处理, 消息队列是进程安全的: 
    - 进程间通讯，应采用消息中间件, 此处计划选用RabbitMQ
    - 程序需要至少有3个进程, 生产者进程、消费者进程、消息队列进程
3. 生产者连续地随机生成任务放入消息队列( 如打印字符串任务、整数加法任务); 使用多态来支持不同种类的任务需求: 
    - 抽象出Task包，来描述任务
    - Task包应该是被生产者、消费者项目共享的公共包
    - Task包至少应包含三个类: Task接口, 打印字符串Task, 整数加法Task
    - Task是可以持久化和被反持久化的, 计划采用pickle库实现持久化和反持久化
4. 生产者需要记录已经完成任务的数量, 如果当前已经完成的任务数量超过1000，那么停止生产:
    - 由于是单消费者, 循环1000次即可
5. 一个完整的程序，包括指明所使用的库（#include/ import等），和相应的程序入口main 函数:
    - 一个完整的程序, 包含生产者、消费者子项目、中间件启动脚本, 考虑采用gradle多项目管理
    - 项目计划提供单脚本启动中间件和一个生产者进程和两个消费者进程，外加RabbitMQ, 共计4个进程
    - 简单原则项目仅依赖rabbitmq客户端库
6. 代码不需要编译运行，尽量保持语法正确。可以上网搜索资料，但不能连续copy超过1行的代码
    - 代码不需要编译运行, 尽量保持语法正确: 还是尽量可以运行的好, 这样语法也会基本正确, 时间不足尽量写简单
7. 每个任务只在一个CPU核心上运行
    - 绑定cpu运行
    
## 开发

- 项目名称: spmc-py （单生产者多消费者示例程序)
- 版本: 1.0.0
- 开发环境: 
    - IDE: pycharm社区版
    - 语言: python3.6
    - 第三方类库: pika, pickle, psutil,（需要: pip install)
    - 中间件: RabbitMQ3.7

## 制品与执行

- 运行环境: python3
- 执行脚本
    - 启动带有管理界面的RabbitMQ中间件:
    ~~~shell
    # 启动带有管理界面的RabbitMQ
    sh 00_rabbitmq.sh
    ~~~
    - 安装pip依赖项
    ~~~
    sh 01_pip_install.sh
    ~~~
    - 启动消费者
    ~~~
    sh 02_consumer.sh
    sh 03_consumer.sh
    ~~~
    - 启动一个生产者
    ~~~
    sh 04_producer.sh
    ~~~
    - 查看使用帮助
    ~~~
    sh 05_help.sh
    ~~~
## 其他

- 帮助信息
~~~shell
python3 spmc/cli.py -h

[*] 帮助信息:
[*]      使用方式:
[*]          python3 cli.py [选项] 命令
[*]      示例:
[*]          以消费者模式启动: python3 cli.py -c
[*]          以生产者模式启动: python3 cli.py -p
[*]      选项:
[*]          -c --cpu 指定cpu运行, 本机可选值: [0, 1, 2, 3, 4, 5, 6, 7]
[*]          -q --queue 指定queue的名称, 默认为spmc.queue
[*]          -s --server 指定消息队列主机的名称, 默认为localhost
[*]      命令:
[*]          -p --producer 以生产者的方式运行
[*]          -c --consumer 以消费者的方式运行
[*]          -v --version 打印版本信息
[*]          -h --help 打印帮助信息
[*]          默认: 打印帮助信息
~~~
- 版本信息
~~~shell
python3 spmc/cli.py -v
[*] 单生产者多消费者示例程序
[*] SPMC
[*] Version 0.0.1
~~~

## TODO 未完成

- 容错、异常处理的细分
- 多进程尽量利用和占满CPU
- 检查如果有其他生产者存在则报错