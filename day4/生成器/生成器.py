# encoding = utf-8
__author__ = "Ang Li"


def cut_off():
    cut_off_flog = "*"
    print(cut_off_flog.ljust(70, '*'))


cut_off()

a = ( i*2 for i in range(10) )
print(a.__next__())
print(a.__next__())

