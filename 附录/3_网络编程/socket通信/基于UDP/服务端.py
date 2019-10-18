# encoding = utf-8
__author__ = "Ang Li"

import socket

phone = socket.socket(socket.AF_INET, socket.SOCK_DGRAM) # 实例化udp对象
phone.bind(("127.0.0.1",8080))

# udp 不用accept建连接了, 可以直接接收消息

while True:
    data,client_addr = phone.recvfrom(1024) # udp 收消息使用recvfrom() , 发消息使用sendto()---> udp 不用链接
                                            # 服务端接收到的udp消息中,含有客户端的ip,接口信息, 所有客户端可以发空消息
    print(data)
    phone.sendto(data.upper(), client_addr) # udp 协议,作为一个数据包协议, 一个send 对应一个 recv, ---> 不会粘包


