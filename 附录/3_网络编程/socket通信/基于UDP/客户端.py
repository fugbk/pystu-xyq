# encoding = utf-8
__author__ = "Ang Li"

import socket


phone = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

while True:
    msg = input(">>> ").strip()
    phone.sendto(msg.encode('utf-8'),("127.0.0.1",8080))

    recv_data, server_addr = phone.recvfrom(1024)

    print(recv_data, server_addr)