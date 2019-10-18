# encoding = utf-8
__author__ = "Ang Li"

import json
import socket
import struct

class MYTCPClient(object):
    address_family = socket.AF_INET
    socket_type = socket.SOCK_STREAM
    coding = 'utf-8'

    def __init__(self,server_address, server_port):
        self.server_address = server_address
        self.server_port = server_port
        self.server_info = (server_address, server_port)
        self.phone_obj = socket.socket(self.address_family, self.socket_type) # 实例化一个socket对象

    def active(self):
        self.phone_obj.connect(self.server_info) # 连接服务端
        print("连接成功.")

    def close_connection(self, connect_obj):
        """关闭连接"""
        connect_obj.close()

    def run(self):
        self.active()
        while True:

            cmd = input("cmd >>> ") # 客户端发送的消息
            if not cmd:continue # 客户端发送的消息, 不能为空, 否则会卡住

            # 发命令
            self.phone_obj.send(cmd.encode(self.coding)) # 以utf-98 格式，编码为二进制格式，传输

            # 第一步：接收报文头部的长度报文, 获取报文头部长度
            obj = self.phone_obj.recv(4)
            header_size = struct.unpack('i',obj)[0] # 进行解封装，解封装完后就是整型，不用解码了
            print("报头长度：", header_size)

            # 第二步：接收报文头部数据, 获取报文数据长度
            header_bytes = self.phone_obj.recv(header_size).decode('utf-8') # 这个报文头部是直接编码二进制发送的，需要先解码
            header_json = json.loads(header_bytes) # 反序列化，获取报文头部数据
            file_size = header_json["file_size"]
            file_name = header_json["file_name"]

            # 第三步：收取报文数据
            print("预接收数据总长度：", file_size)

            # 根据接收到的数据长度，开始接收数据
            recv_size = 0 # ---> 接收到的数据长度
            with open(file_name,'wb+') as f:
                while recv_size < file_size: # 如果接收的数据，小于预接收数据，则继续接收
                    data = self.phone_obj.recv(1024)
                    f.write(data)
                    recv_size += len(data) # 计算为解码前的数据长度
                    print("数据总长度: %s ,已接收的数据长度：%s" %(file_size, recv_size))

        self.close_connection(self.phone_obj)


client1 = MYTCPClient("127.0.0.1",8086)
client1.run()