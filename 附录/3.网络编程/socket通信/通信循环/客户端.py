# encoding = utf-8
__author__ = "Ang Li"

import socket

# 实例化一个对象
phone = socket.socket(socket.AF_INET,socket.SOCK_STREAM)

# 通过这个套接字对象, 连接服务端socket
phone.connect(("127.0.0.1",8080))
print("开始连接...")

while True:
    msg = input("msg >>> ") # 客户端发送的消息
    if not msg:continue # 客户端发送的消息, 不能为空, 否则会卡住

    # 通过这个套接字 , 发送消息
    phone.send(msg.encode('utf-8'))

    # 接收消息, 最大接收1024 个字节的消息
    data = phone.recv(1024).decode('utf-8')
    print("服务端返回的消息:", data)

phone.close()