# encoding = utf-8
__author__ = "Ang Li"
import os

url = 'https://v1.hitokoto.cn/?c=d&charset=utf-8'
a = os.popen('curl %s' %url).readlines()

print(a)
