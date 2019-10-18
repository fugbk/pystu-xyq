# encoding = utf-8
__author__ = "Ang Li"

import json
import os
import socket
import struct  # 用于填充数据包

class MYTCPServer(object):
    address_family = socket.AF_INET
    socket_type = socket.SOCK_STREAM
    coding = 'utf-8'
    request_queue_size = 5

    def __init__(self,server_address, server_port):
        self.server_address = server_address
        self.server_port = server_port
        self.phone_obj = socket.socket(self.address_family, self.socket_type)
        print("生成socket 对象:", self.phone_obj)
        self.phone_obj.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)  # 一行代码搞定，写在bind之前

    def active(self):
        """绑定地址, 并启动监听"""
        self.phone_obj.bind((self.server_address, self.server_port))
        print("绑定地址: ", self.server_address, self.server_port)
        # 启动监听
        self.phone_obj.listen(self.request_queue_size)
        print("启动监听...")

    def close_connect(self, connect_obj):
        """关闭链接, 需传入链接对象"""
        connect_obj.close()

    def push(self):
        """文件上传"""
        pass

    def run(self):
        """控制器, 用于组织命令收取, 报头发送, 数据发送"""
        self.active()
        while True: # 可接收多个链接
            # 被动接受TCP客户的连接,(阻塞式)等待连接的到来, 这时候返回的是一个元组(连接对象, 客户端地址)
            conn, client_addr = self.phone_obj.accept() # 当一个连接break之后，程序回到这里，接入下一个连接
            print(client_addr)

            while True:

                recv_res = conn.recv(1024).decode('utf-8')
                if not recv_res:break
                print("收到命令：", recv_res)

                # 第一步：解析出来请求的命令，及要下载的文件
                recv_list = recv_res.split()
                recv_cmd, recv_file = recv_list
                print(recv_cmd, recv_file)

                # 第二步：获取文件大小，定义头部信息
                file_size = os.path.getsize(recv_file)
                header_dic = {
                    "file_name": recv_file,
                    "md5": 22222222222222222,
                    "file_size": file_size
                }

                header_json = json.dumps(header_dic)
                header_bytes = header_json.encode('utf-8')
                header_size = len(header_bytes)
                print("报头长度：", header_size, type(header_size))

                # 第三步：发送报文头部长度，这里的报文头部长度还是整型，通过struct 包装为 4 byte 的二进制格式
                conn.send(struct.pack('i', header_size))

                # 第四步：发送报文头部数据
                conn.send(header_bytes)
                print("发送报文头部数据...")
                print("下载文件长度：", file_size)

                # 第五步：发送报文数据, 逐行读取文件长度，并发送
                with open(recv_file,'rb') as f:
                    for line in f:
                        conn.send(line)

            # 关闭链接
            self.close_connect(conn)

        self.close_connect(self.phone_obj)


server1 = MYTCPServer('127.0.0.1',8086)
server1.run()