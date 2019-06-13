# Author: LiAng
# encoding = utf-8
# Email : ali6102@163.com

import time

time_man = '%Y-%m-%d %X'
time_current = time.strftime(time_man)

print(time_current)

def log():
    "log file"
    with open('a.txt','a+') as f:
        f.write('%s start test\n' %time_current)

def test1():
    "test 1"
    print('test 1')
    log()

def test2():
    "test 2"
    print('test 2')
    log()

test1()
test2()