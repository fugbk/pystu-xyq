# encoding = utf-8
__author__ = "Ang Li"

import hashlib

def hmac_test():
    import hmac
    h = hmac.new('天王盖地虎'.encode(encoding="utf-8"), b'125dfsfax')   # 这些汉字需要编码成utf-8 格式
    print(h.hexdigest())

hmac_test()


def sha1_test():
    hash_test = hashlib.sha1()
    hash_test.update(b'admin')
    print(hash_test.hexdigest())


def md5_test():
    m = hashlib.md5()   # 先生成一个hashlib对象
    m.update(b"Hello Word")   # 添加一个值,也就是要加密的数据,必须时"二进制" 的.
    print(m.hexdigest())   # 打印16进制的加密后的数据

    m.update(b"I'm fine, think you.")   # 如果在向这个对象中添加数据,则是追加到前面的数据上.
    print(m.hexdigest())





