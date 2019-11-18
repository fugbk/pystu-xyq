# encoding = utf-8
__author__ = "Ang Li"
# 多url ， 添加图片

from wsgiref.simple_server import make_server
import re,os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))


def login(environ, start_response):
    start_response("200 OK", [('Content-Type', 'text/html;charset=utf-8')])
    html = """
        <form method="post">
            <input type="text" name="username">
            <input type="password" name="password">
            <input type="submit" value="登录">
            <input type="checkbox" value="Remember me!">
        </form>
    """
    return [bytes(html, encoding='utf-8')]


def book(environ, start_response):
    start_response("200 OK", [('Content-Type', 'text/html;charset=utf-8')])
    return [bytes('<h1 style="color:red">book</h1>', encoding="utf-8")]


def cloth(environ, start_response):
    start_response("200 OK", [('Content-Type', 'text/html;charset=utf-8')])
    return [bytes('<h1 style="color:blue">cloth</h1>', encoding='utf-8')]


def img_handel(request_url):
    img_dir = os.path.join(BASE_DIR, "static_data")
    img_name = re.sub("/static/", "", request_url)
    img_path = os.path.join(img_dir, img_name)
    print(img_path)
    if os.path.isfile(img_path):
        with open(img_path, 'rb') as f:
            img_data = f.read()
        return [img_data, 0]
    return [None, 1]


def img_test(environ, start_response):
    html = """
        <h1>欢迎来到图片专区</h1>
        
        <script type="text/javascript">
         
        function Student(name, age){
            this.name = name;
            this.age = age;
            this.description = function(){
                return this.name + "的年龄是：" + this.age;
            }
        }
         
        var p4 = new Student("Tony", 28);
        var p5 = new Student("Tom", 40);
        console.log(p4.description())	//输出为：Tony的年龄是：28
        console.log(p5.description())	//输出为：Tom的年龄是：40
         
        </script>

        <img src='/static/1.jpg' />
        <p>更多内容 www.mcabana.com</p>
    """
    start_response("200 OK", [('Content-Type', 'text/html;charset=utf-8')])
    return [bytes(html, encoding='utf-8')]


def js_test(environ, start_response):
    html = """
        <h1 style="color:red">test</h1>
        <div class="pink fontWeight font20">亚瑟</div>
        <div class="font20">刘备</div>
        <div class="font14 pink">安其拉</div>
        <div class="font14">貂蝉</div>
        <!doctype html>
        <html>
        <head>
        <meta charset="utf-8">

        <script type="text/javascript">
         
        function Student(name, age){
            this.name = name;
            this.age = age;
            this.description = function(){
                return this.name + "的年龄是：" + this.age;
            }
        }
         
        var p4 = new Student("Tony", 280);
        var p5 = new Student("Tom", 400);
        console.log(p4.description())	//输出为：Tony的年龄是：280
        console.log(p5.description())	//输出为：Tom的年龄是：400
         
        </script>

        </head>
        </html>
    """
    start_response("200 OK", [('Content-Type', 'text/html;charset=utf-8')])
    return [bytes(html, encoding='utf-8')]


def page_not_found(environ, start_response):
    start_response("404 Error", [('Content-Type', 'text/html;charset=utf-8')])
    return [bytes('<h1 style="color:blue"> 404 page not found</h1>', encoding='utf-8')]


def urls():
    urls = {
        "/book": book,
        "/cloth": cloth,
        "/login/": login,
        "/img_test": img_test,
        "/23": js_test,
    }
    return urls


def run_server(environ, start_response):
    request_url = environ["PATH_INFO"]
    url_list = urls()
    if request_url in url_list:
        func_data = url_list[request_url](environ, start_response)
    elif request_url.startswith("/static/"):
        print("--------------->")
        img_data, img_status = img_handel(request_url)
        start_response("200 OK", [('Content-Type', 'text/jpeg;charset=utf-8')])
        func_data = [img_data,]
    else:
        func_data = page_not_found(environ, start_response)
    return func_data


s = make_server('localhost', 8000, run_server)
s.serve_forever()