# encoding = utf-8
__author__ = "Ang Li"


def cut_off():
    cut_off_flog = "*"
    print(cut_off_flog.ljust(70, '*'))


cut_off()



a = [ x+2 for x in range(100000) ]
print(a[1])