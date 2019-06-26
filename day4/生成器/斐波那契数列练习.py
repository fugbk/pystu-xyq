# encoding = utf-8
__author__ = "Ang Li"


def cut_off():
    cut_off_flog = "*"
    print(cut_off_flog.ljust(70, '*'))
cut_off()

def fib(max):
    a,b,n = 0,1,0
    while n < max:
        #print(b)
        yield b
        a,b=b,a+b
        n += 1
    return '--done--'
g = fib(10)

while True:
    try:
        x = next(g) #next的方法，《==》__next__()
        print("g: ",x)
    except StopIteration as e: # e --> try 和expect之间的错误代码
                                # e中包含Stop。。。
        print("error",e.value)
        break

