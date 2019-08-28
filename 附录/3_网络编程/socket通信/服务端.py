# encoding = utf-8
__author__ = "Ang Li"

import socket
# 生成一个socket 对象
phone = socket.socket(socket.AF_INET,socket.SOCK_STREAM)

# 绑定地址,端口号 (这是一个元组格式的)
phone.bind(("127.0.0.1",8080))

# 开启监听, (5)--> socket的最大连接数
phone.listen(5)
print("启动监听...")

# 被动接受TCP客户的连接,(阻塞式)等待连接的到来, 这时候返回的是一个元组(连接对象, 客户端地址)
conn,client_addr = phone.accept()

# 通过返回的连接对象, 接收客户端消息, 最大接收1024 个字节的消息; 此时服务端有两个 套接字对象
data = conn.recv(1024)

# 发送消息, 先发送一个大写消息
conn.send(data.upper())

# 关闭链接
conn.close()
phone.close()