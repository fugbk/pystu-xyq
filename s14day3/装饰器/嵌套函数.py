# Author: LiAng
# encoding = utf-8
# Email : ali6102@163.com


#
# def foo():
#     print('in the foo')
#     def bar():
#         print('in the bar')
#     bar()
#
# foo()

def logger(func):
    print("logger")
    func()
def bar():
    print("in the bar")

logger(bar)

print('--------------------------------------')


def logger(func):
    def wrapper(*args,**kwargs):
        print('logger')
        return func(*args,**kwargs)
    return wrapper()

@logger
def bar():
    print('in the bar')

