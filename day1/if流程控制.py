# Author：Li Ang
# encoding=utf8
'''
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
'''
#if elif 多重判断

age = 20
guess_age = int(input("guess_age:")) #py3中input 默认输入的是字符串，需要转换为整形。
if guess_age == age:  #两个等号代表等于判断，一个等号 是赋值
    print("Yes ,you got it...")
elif guess_age > age:
    print("No,think bigger!")
else:
    print("No,think smaller!")



"""
python的if判断 要求 强缩进，因此没有结束符
1. 节省代码
2. 条理清晰
"""

