# encoding = utf-8
__author__ = "Ang Li"
from wsgiref.simple_server import make_server
"""
基本逻辑：
a. 接收客户端请求，提取访问的url
b. 检查请求url，找到访问的页面
c. 将页面封装进 http报文，返回给客户端
"""


def book(environ, start_response):
    print("book page")
    start_response("200 OK", [('Content-Type', 'text/html;charset=utf-8')])
    return [bytes('<h1 style="color:red">book page</h1>', encoding='utf-8')]


def cloth(environ, start_response):
    print("cloth page")
    start_response("200 OK", [("Conetnt-Type", 'text/html;charset=utf-8')])
    return [bytes('<h2 style="color:blue">cloth page</h2>', encoding='utf-8')]


def page_not_found(environ, satrt_response):
    print("404 page not found")
    satrt_response("404 Not Found", [('Content-Type', 'text/html;charset=utf-8')])
    return [bytes('<h3 style="color:blue">404 page not found<h3>', encoding='utf-8')]


def url_dispacher():
    url_list = {
        "/book": book,
        "/cloth": cloth,
    }
    return url_list


def run_server(environ, start_response):
    """
    :param environ:  mk_server() 传递进来的参数，是浏览器（客户端）发来的的自己的请求信息
    :param start_response: 也是mk_server() 传递进来的的，是一个实例，用于构造http包
    :return: 返回发送给客户端的数据
    """
    request_url = environ.get("PATH_INFO") # PATH_INFO是请求url
    url_lsit = url_dispacher()
    if request_url in url_lsit:
        func_data = url_lsit[request_url](environ, start_response)
        return func_data
    else:
        func_data = page_not_found(environ, start_response)
        return func_data

# 使用make_server 创建这个s对象，传递参数是固定格式的
s = make_server('localhost', 8000, run_server)

# 重复接收请求
s.serve_forever()