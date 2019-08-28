# encoding = utf-8
__author__ = "Ang Li"

import socket

# 实例化一个对象
phone = socket.socket(socket.AF_INET,socket.SOCK_STREAM)

# 通过这个套接字对象, 连接服务端socket
phone.connect(("127.0.0.1",8080))

# 通过这个套接字 , 发送消息
phone.send("hello".encode('utf-8'))

# 接收消息, 最大接收1024 个字节的消息
data = phone.recv(1024)

print("服务端返回的消息:", data)

phone.close()