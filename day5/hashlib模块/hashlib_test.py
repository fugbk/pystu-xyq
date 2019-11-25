# encoding = utf-8
__author__ = "Ang Li"

import hashlib

m = hashlib.md5()   # 先生成一个hashlib对象
m.update(b"Hello Word")   # 添加一个值,也就是要加密的数据,必须时"二进制" 的.
print(m.hexdigest())   # 打印16进制的加密后的数据

m.update(b"I'm fine, think you.")   # 如果在向这个对象中添加数据,则是追加到前面的数据上.
print(m.hexdigest())



