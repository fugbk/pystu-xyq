# encoding = utf-8
__author__ = "Ang Li"

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

    # 2、接收命令执行结果的长度，准备多次接收
    header = phone.recv(4)
    print(len(header))
    total_size = struct.unpack('i',header)[0] # 解包，并获取总长度---> 预接收长度
    print("预接收数据总长度：", total_size)

    # 3、根据接收到的数据长度，开始接收数据
    recv_data = b'' # ---> 保存所有接收的数据, 因为发来的数据是二进制格式的，这里拼接的recv_data 也得是二进制格式
    recv_size = 0 # ---> 接收到的数据长度
    while recv_size < total_size: # 如果接收的数据，小于预接收数据，则继续接收
        data = phone.recv(1024)
        recv_data += data
        recv_size += len(data) # 计算为解码前的数据长度
        print("已接收的数据长度：",recv_size)
    print(recv_data.decode('gbk')) # 将拼接完的二进制的数据，解码（win-gbk）
phone.close()