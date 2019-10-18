# encoding = utf-8
__author__ = "Ang Li"

import socket

def main():
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    sock.bind(('localhost', 8000))
    sock.listen(5)

    while True:
        # 等待客户端连接
        conn, addr = sock.accept()
        print(conn)
        print(addr)
        # 接收客户端请求
        data = conn.recv(1024)
        print(data)

        # 给客户端返回数据
        conn.send(b"HTTP/1.1 200 OK\r\nContent-Type:text/html; charset=utf-8\r\n\r\n")
        conn.send("<h1 style='color:red'>这是一个测试!</h1>".encode('utf-8'))

        conn.close()

if __name__ == "__main__":
    main()

