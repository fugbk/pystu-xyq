# Author：Li Ang
# encoding=utf8

'''
#.format使用
a = 1
b = 2

print("who is {a1} and who is {b1}".format(a1=int(a),b1=int(b)))

a = chr(a)

print(type(a),type(b))
'''

import sys
import os
name = input("name:")
age = int(input("age:"))


print(type(age),os.popen(str(age)))
print(type(age))
print(os.popen(str(age)))

print(os.popen(int(age)))
job = input("job:")
salary = input("salary:")
info = '''
--------------info%s---------------
name:%s
age:%d
job:%s
salary:%s
'''%(name,name,age,job,salary)
print(info)