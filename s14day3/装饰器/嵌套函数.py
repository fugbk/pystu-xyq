# Author: LiAng
# encoding = utf-8
# Email : ali6102@163.com



def foo():
    print('in the foo')
    def bar():
        print('in the bar')
    bar()

foo()