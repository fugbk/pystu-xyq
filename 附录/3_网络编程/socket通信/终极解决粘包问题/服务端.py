# encoding = utf-8
__author__ = "Ang Li"

import json
import socket
import struct  # 用于填充数据包
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

        cmd = conn.recv(1024).decode('utf-8')
        if not cmd:break
        print("收到命令：", cmd)

        obj = subprocess.Popen(cmd, shell=True,
                               stdout=subprocess.PIPE,
                               stderr=subprocess.PIPE)
        stdout = obj.stdout.read() # 正确的结果信息，这里的结果信息本身就是二进制格式
        stderr = obj.stderr.read() # 错误的结果信息，这里的结果信息本身就是二进制格式
        total_size = len(stdout + stderr)

        # 第一步：定义一个头部信息
        header_dic = {
            "file_name": "xxxx",
            "md5": 22222222222222222,
            "total_size": total_size
        }
        header_json = json.dumps(header_dic) # 通过json 将数据序列化为字符串
        header_bytes = header_json.encode('utf-8') # 将报文头部以 utf-8 格式编码为 二进制
        header_size = len(header_bytes)
        print("报头长度：", header_size, type(header_size))

        # 第二步：发送报文头部长度，这里的报文头部长度还是整型，通过struct 包装为 4 byte 的二进制格式
        conn.send(struct.pack('i', header_size))

        # 第三步：发送报文头部数据
        conn.send(header_bytes)
        print("发送报文头部数据...")
        print("报文数据长度：", total_size)

        # 第三步：发送报文数据，借助TCP 的粘包，都发送出去---> 客户端收取的数据长度是正确信息和错误信息
        conn.send(stdout)
        conn.send(stderr)

    # 关闭链接
    conn.close()

phone.close()
