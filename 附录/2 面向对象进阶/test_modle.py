# encoding = utf-8
__author__ = "Ang Li"

import 反射
if hasattr(反射,"p"):
    o = getattr(反射,"p")
    print(o)
    print(o.name)
    o.talk()