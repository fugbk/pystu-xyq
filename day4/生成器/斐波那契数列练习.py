# encoding = utf-8
__author__ = "Ang Li"


def cut_off():
    cut_off_flog = "*"
    print(cut_off_flog.ljust(70, '*'))
cut_off()

def fib(max):
    a,b,n = 0,1,0
    while n < max:
        print(b)
        c = b
        b = a + b
        a = c
        n += 1
fib(10)
