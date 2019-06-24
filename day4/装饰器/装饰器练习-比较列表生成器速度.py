# encoding = utf-8
__author__ = "Ang Li"


def cut_off():
    cut_off_flog = "*"
    print(cut_off_flog.ljust(70, '*'))


cut_off()

import time
def timer(func):
    def wrapper(*args,**kwargs):
        start_time = time.time()
        func(*args,**kwargs)
        stop_time = time.time()
        print("func run time is %s" %(stop_time - start_time))
    return wrapper

@timer # 列表生成式
def list():
    a = [ i+2 for i in range(100000000) ]
list()

@timer # 列表生成器
def list2():
    a = ( i+2 for i in range(100000000) )
list2()