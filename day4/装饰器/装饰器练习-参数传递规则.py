# encoding = utf-8
__author__ = "Ang Li"

#-----------------------------------------------------------------------------------------------

user,passw = "ali","123"
def auth(auth_type): # 传递的装饰器本身的参数
    def out_wrapper(func):  # 传递被装饰的函数内存地址
        def wrapper(*args,**kwargs): # 传递被装饰函数 的 本身形参
            if auth_type == "local":
                print("use local authcation!")
                username = input("username: ").strip()
                password = input("password: ").strip()
                if user == username and passw == password:
                    func(*args,**kwargs)
                    print("Authcation success.")
                else:
                    exit ("Invalid error!")
            elif auth_type == "ldap":
                print("use ldap authcation")
        return wrapper
    return out_wrapper

def index():
    print("in the index.")

@auth("local")
def home():
    print("in the home")

@auth(auth_type="ldap")
def var():
    print("in the var.")

index()
home()
var()
