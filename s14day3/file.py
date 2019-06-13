# Author: LiAng
# encoding = utf-8
# Email : ali6102@163.com

'''
f = open("yesterday2",'a')

f.write("同九年\n")
f.write("汝何秀")

data = f.read()
print(data)

f.close()



f =  open("yesterday",'r')

# for i in range(4):
#     print(f.readline())

for index,line in enumerate(f.readlines()):
    if index == "9":
        continue
    print(line.strip())

count = 0           # 定义一个计数器
for line in f: #直接循环这个文件句柄， 会一次只读一行， 在内存中只保留一行的内容；
    count += 1
    if count == "10":
        print("-----------------第十行---------------------")
        continue
    print(line)
f.close()


f =  open("yesterday",'r')
print(f.tell())
print(f.readline())
print(f.readline())
print(f.tell())
print(f.readline())

f.seek(0)
print(f.tell())
print(f.readline())

print(f.encoding)

print(f.fileno())
print(f.isatty())
print(f.seekable()) # 判断一个文件，是否可以移动指针， 并非所有文件都可以移动指针； 设备文件， tty 等文件
# 都不可以移动指针；

print(f.readable()) # 判断文件是否可读；
print(f.writable()) #判断文件是否可写；



# 进度条
import sys,time
for i in range(30):
    sys.stdout.write("# ")  # 标准输出到屏幕
    sys.stdout.flush()      # 没输出一个， 就刷新
    time.sleep(0.2)         # sleep 0.2


f = open("yesterday2",'wb')
f.write("hello , word".encode())
f.close()


f = open("yesterday",'r')      # <==  要修改的文件，只读
f_new = open("yesterday2",'w')      #<== 新文件 覆盖写

for line in f:
    if "有那么多肆意的快乐等我享受" in line:
        #line = "有那么多肆意的快乐等liAng享受\n"       # <== 直接替换整行
        line = line.replace('我','liAng')        # <== 直接替换字符串 .replace(old,new)
        print(line)
    f_new.write(line)
f.close()
f_new.close()


import sys
find_str = sys.argv[1]      # <== 第一个参数是查找的内容
replace_str = sys.argv[2]       #<== 第二个参数 是替换后的内容

f = open("yesterday",'r')
f_new = open("yesterday2",'w')

for line in f:
    if find_str in line:
        line = line.replace(find_str,replace_str)   # <== 直接替换
    f_new.write(line)

'''

with open("yesterday",'r') as f , \
        open("yesterday2",'w') as f_new:    # <== 打开多个文件，都好分隔，\ 表示换行
    for line in f:      # <== 后续语法的缩进，要在with后面
        if "我" in line:
            line = line.replace('我','liAng')
        f_new.write(line)
