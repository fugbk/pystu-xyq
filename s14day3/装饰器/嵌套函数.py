# Author: LiAng
# encoding = utf-8
# Email : ali6102@163.com


def foo():
    print('in the foo')
    def bar():
        print('in the bar')
    bar()

foo()

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
print('--------------------------------------')

def grandpa():
    x = "I'm grandpa."
    print(x)
    def dad():
#        x = "I'm dad."
        print(x)
        def son():
            x = "I'm son"
            print(x)
        son()
    dad()
grandpa()
