# encoding = utf-8
__author__ = "Ang Li"

import json
import socket
import struct

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

    # 第一步：接收报文头部的长度报文, 获取报文头部长度
    obj = phone.recv(4)
    header_size = struct.unpack('i',obj)[0] # 进行解封装，解封装完后就是整型，不用解码了
    print("报头长度：", header_size)

    # 第二步：接收报文头部数据, 获取报文数据长度
    header_bytes = phone.recv(header_size).decode('utf-8') # 这个报文头部是直接编码二进制发送的，需要先解码
    header_json = json.loads(header_bytes) # 反序列化，获取报文头部数据
    total_size = header_json["total_size"]

    # 第三步：收取报文数据
    print("预接收数据总长度：", total_size)

    # 根据接收到的数据长度，开始接收数据
    recv_data = b'' # ---> 保存所有接收的数据, 因为发来的数据是二进制格式的，这里拼接的recv_data 也得是二进制格式
    recv_size = 0 # ---> 接收到的数据长度

    while recv_size < total_size: # 如果接收的数据，小于预接收数据，则继续接收
        data = phone.recv(1024)
        recv_data += data
        recv_size += len(data) # 计算为解码前的数据长度

    print("已接收的数据长度：", recv_size)
    print(recv_data.decode('gbk')) # 将拼接完的二进制的数据，解码（win-gbk）

phone.close()