# Author: LiAng
# encoding = utf-8
# Email : ali6102@163.com

def cut_off():
    cut_off_flog = "*"
    print(cut_off_flog.ljust(70,'*'))
cut_off()


def add(a,b,f):
    return f(a) + f(b)
c = add(-3,-4,abs)

print(c)
print(cut_off)
#-------------------------------------------------------------------------

import time
def test():
    time.sleep(1)
    print("in the test")

def bar(func):
    start_time = time.time()
    stop_time = time.time()
    print("the func run time is %s" %(stop_time - start_time))
    return func

test = bar(test)
test()
print(cut_off)
#---------------------------------------------------------------------------

import time
def test2():
    print("in the test2")

def foo(func):
    print(time.time())
    return func

test2 = foo(test2)
test2()
