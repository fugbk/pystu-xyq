# encoding = utf-8
__author__ = "Ang Li"
from wsgiref.simple_server import make_server

def run_server(environ, start_response):
    """
    :param environ:  mk_server() 传递进来的参数，是浏览器（客户端）发来的的自己的请求信息
    :param start_response: 也是mk_server() 传递进来的的，是一个实例，用于构造http包
    :return: 返回发送给客户端的数据
    """
    """
    向这个实例传入固定格式的参数，构造http报文
    这是个元组(状态码,类型)
    """
    start_response("200 OK", [('Content-Type', 'text/html;charset=utf-8')])

    """
    通过return返回个 客户端的数据，make_server 会接收这个return信息，并使用前面构造的http报文
    start_response，发送给客户端
    返回的固定格式的信息，二进制格式的
    """
    return [bytes('<h1 style="color:green">这是个测试！</h1>\r\n<h1 style="color:red">这也是个 测试</h1>',encoding='utf-8'),]

# 使用make_server 创建这个s对象，传递参数是固定格式的
s = make_server('localhost', 8000, run_server)

# 重复接收请求
s.serve_forever()