# Author：Li Ang
# encoding=utf8

_username = "li"
_password = "123"
username = input("Username:")
password = input("Password:")
if username == _username and password == _password:
    #print("Wellcome user " ,username, "login ...." )
    #当变量和常量同时输出时常量需要用双引号，变量用双逗号
    print("Wellcome user {name} login...".format(name=username))
    #.format 的用法之一
else:
    print("Invalid username or password")