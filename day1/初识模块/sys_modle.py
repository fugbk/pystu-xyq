# Author：Li Ang
# encoding=utf8
'''
import sys
#print(sys.path)
print(sys.argv)
print(sys.argv[2])
'''

import sys

#cmd_dir = print(os.system("dir"))
#cmd_dir = print(os.popen("dir").read())
#print("---->",cmd_dir)
print(sys.path)

print(sys.argv)

import os
print(os.system("dir"))

test = os.system("dir")
print("-------------")
print(test)

cmd_dir = os.popen("dir").read()
print("_______")

print(cmd_dir)
