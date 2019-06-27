# encoding = utf-8
__author__ = "Ang Li"

def cut_off():
    cut_off_flog = "*"
    print(cut_off_flog.ljust(70, '*'))

cut_off()

from collections import Iterable

isinstance({},Iterable)
isinstance(( x*2 for x in range(10)),Iterable)

