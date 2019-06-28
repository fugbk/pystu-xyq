# encoding = utf-8
__author__ = "Ang Li"


def cut_off():
    cut_off_flog = "*"
    print(cut_off_flog.ljust(70, '*'))


cut_off()

#匿名函数：
calc = lambda n:3 if n < 4 else 5
print(calc(3))

dirc = ""

res = filter(lambda x:x>5,range(10))

for i in res:
    print(i)
cut_off()
res2 = map(lambda c:c*c,range(10))
for i in res2:
    print(i)

res2 = ( c*c for c in range(10))
cut_off()

import functools
res = functools.reduce(lambda x,y:x+y,range(10))
print(res)