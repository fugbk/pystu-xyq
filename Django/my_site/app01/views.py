from django.shortcuts import HttpResponse,render

# Create your views here.

def index_view(requeset):
    html = """
        <h1 style='color:red'>Wellcome ！</h1>
    """
    return HttpResponse(html)


def index(request):
    return render('index.html')

def test_view(request):
    print('执行业务逻辑，计算第一次多少钱。')
    print(dir(request))
    return HttpResponse("<h1 style='color:red'>500一次！</h1>")


def login_view(request):
    return render(request, "login.html")


def do_login(request):
    username = request.POST.get('username')
    password = request.POST.get('password')
    print(username+"  "+password)
    if username == 'admin' and password == '123456':
        return render(request, 'zhihu/index.html')
    else:
        return render(request, 'zhihu/login.html', {
            'username': username,
            'password': password
        })
