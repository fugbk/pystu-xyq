# encoding = utf-8
__author__ = "Ang Li"

import socket
import subprocess

# 生成一个socket 对象
phone = socket.socket(socket.AF_INET,socket.SOCK_STREAM)

phone.setsockopt(socket.SOL_SOCKET,socket.SO_REUSEADDR,1) #一行代码搞定，写在bind之前

# 绑定地址,端口号 (这是一个元组格式的)
phone.bind(("127.0.0.1",8080))

# 开启监听, (5)--> socket的最大连接数
phone.listen(5)
print("启动监听...")

while True: # 可接收多个链接
    # 被动接受TCP客户的连接,(阻塞式)等待连接的到来, 这时候返回的是一个元组(连接对象, 客户端地址)
    conn, client_addr = phone.accept() # 当一个连接break之后，程序回到这里，接入下一个连接
    print(client_addr)

    while True:
        # 1. 收取命令， 因为执行命令是字符串，需要解码为 字符串；
        cmd = conn.recv(1024).decode('utf-8')
        if not cmd:break
        print("收到命令:", cmd)

        # 2. 执行命令， 通过subprocess 模块执行， 并分别保存正确，错误 结果信息到管道
        # 执行命令这里，不能使用 os.system ，因为这样会返回的执行结果只是 状态码
        obj = subprocess.Popen(cmd, shell=True,
                               stdout=subprocess.PIPE,
                               stderr=subprocess.PIPE)
        stdout = obj.stdout.read() # 正确的结果信息，这里的结果信息本身就是二进制格式
        stderr = obj.stderr.read() # 错误的结果信息，这里的结果信息本身就是二进制格式

        print(len(stdout + stderr))

        # 3. 发送消息, 先发送一个大写消息
        conn.send(stdout + stderr) # + 还可以优化

    # 关闭链接
    conn.close()
phone.close()

