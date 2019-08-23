# encoding = utf-8
__author__ = "Ang Li"

class User(object):

    def login(self):
        print("Wellcome login")

    def save(self):
        print("save succeed.")

    def query(self):
        print("query succeed.")

u = User()
flag = True
while flag:
    user_cmd = input(">>> ").strip()
    if hasattr(u,user_cmd):
        func = getattr(u,user_cmd)
        func()
    else:
        print("input error.")
    if user_cmd == "q":
        flag = False