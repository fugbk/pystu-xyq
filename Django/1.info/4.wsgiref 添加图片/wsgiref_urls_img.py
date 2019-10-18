# encoding = utf-8
__author__ = "Ang Li"

import os
import re
from wsgiref.simple_server import make_server

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
img_base = os.path.join(BASE_DIR, "static_data", "img")

"""
基本逻辑：
a. 接收客户端请求，提取访问的url
b. 检查请求url，找到访问的页面
c. 将页面封装进 http报文，返回给客户端
d. 如果请求的url 以/static/开头，则是访问的图片
e. 提取图片名称，构成本地的图片路径
f. 读取图片，返回给客户端
"""

def img_handle(request_url):
    """
    处理发送的请求，获取图片内容
    :param request_url:
    :return: 图片的二进制数据
    """
    img_name = re.sub("/static/", "", request_url) # 提取url中的 图片名称
    img_path = os.path.join(img_base, img_name) # 使用图片名称，结合图片目录，生产图片路径
    if os.path.isfile(img_path): # 如果图片存在
        with open(img_path, 'rb') as f:
            img_data = f.read()
        return [img_data, 0] # 0-->存在
    return [None, 1] # 1 --> 不存在


def book(environ, start_response):
    print("book page")
    start_response("200 OK", [('Content-Type', 'text/html;charset=utf-8')])
    data = '''
        <h1>欢迎来到图片专区</h1>
        <img src='/static/001.jpg' />
        <p>更多内容 www.mcabana.com</p>
    '''
    return [bytes(data, encoding='utf-8')]


def cloth(environ, start_response):
    print("cloth page")
    start_response("200 OK", [("Conetnt-Type", 'text/html;charset=utf-8')])
    return [bytes('<h2 style="color:blue">cloth page</h2>', encoding='utf-8')]


def page_not_found(environ, satrt_response):
    print("404 page not found")
    satrt_response("404 error", [('Content-Type', 'text/html;charset=utf-8')])
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
    url_list = url_dispacher()
    if request_url in url_list:
        func_data = url_list[request_url](environ, start_response)
        return func_data
    elif request_url.startswith("/static/"):
        img_data, img_status = img_handle(request_url)
        if img_status == 0:
            start_response("200 OK", [('Content-Type', 'text/jpeg;charset=utf-8')])
            return [img_data]
        return [bytes('<h1 style="color:red">404 page not found</h1>')]
    else:
        func_data = page_not_found(environ, start_response)
        return func_data

# 使用make_server 创建这个s对象，传递参数是固定格式的
s = make_server('localhost', 8000, run_server)

# 重复接收请求
s.serve_forever()



 
