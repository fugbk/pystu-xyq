from django.shortcuts import HttpResponse

# Create your views here.

def test_view(request):
    print('执行业务逻辑，计算第一次多少钱。')
    return HttpResponse("<h1 style='color:red'>500一次！</h1>")


def login_view(request):
    html = """
        <form method="post">
            <input type="text" name="username">
            <input type="password" name="password">
            <input type="submit" value="登录">  
        </form>
    """
    return HttpResponse(html)