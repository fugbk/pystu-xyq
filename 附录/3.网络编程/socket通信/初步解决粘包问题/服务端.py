# encoding = utf-8
__author__ = "Ang Li"

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

        # 1、先将数据长度，封装成一个固定长度的包， 发送给客户端
        total_size = len(stdout+stderr)
        print("数据长度：",total_size)
        header = struct.pack('i',total_size) # 字符串格式进行封装，封装后的本身就是二进制的
        print("报头长度：",len(header))
        print("\n")
        conn.send(header)

        # 2、发送数据, 借助TCP 的粘包，都发送出去---> 客户端收取的数据长度是正确信息和错误信息
        conn.send(stdout)
        conn.send(stderr)

    # 关闭链接
    conn.close()

phone.close()
