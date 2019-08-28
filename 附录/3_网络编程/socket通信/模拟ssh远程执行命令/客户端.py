# encoding = utf-8
__author__ = "Ang Li"

import socket

# 实例化一个对象
phone = socket.socket(socket.AF_INET,socket.SOCK_STREAM)

# 通过这个套接字对象, 连接服务端socket
phone.connect(("127.0.0.1",8080))
print("开始连接...")

while True:

    cmd = input("cmd >>> ") # 客户端发送的消息
    if not cmd:continue # 客户端发送的消息, 不能为空, 否则会卡住

    # 1、发命令
    phone.send(cmd.encode('utf-8')) # 以utf-98 格式，编码为二进制格式，传输

    # 2、接收命令执行结果， 这里的返回信息可能不止 1024 字节
    res = phone.recv(1024).decode('gbk') # 服务端在windows 上，需要gbk 解码
    print("服务端返回的消息:", res)

phone.close()