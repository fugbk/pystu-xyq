# Author: LiAng
# encoding = utf-8
# Email : ali6102@163.com


def add(a,b,f):
    return f(a) + f(b)
c = add(-3,-4,abs)

print(c)

