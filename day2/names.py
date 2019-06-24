# Author：Li Ang
# encoding=utf8

names = "ZhangYang GuYun XiangPeng XuLiangcheng"
names = ["ZhangYang","GunYun","XiangPeng","XuLiangchen"]
'''
print(names[0],names[1])
print(names[1:2])  #切片 ： 左闭右开
print(names[1:4])
print(names[0:3])   # 左闭第一位到第三位，不包含第三位
print(names[:3])     #如果左边是0 可以省略

print(names[-1])      #右边第一个 -2 -3 -4

print(names[-3:-1])      #列表切片时从左往右数，冒号左边的开始数

print(names[-3:])         #-3:  从右边第三个开始数，一直到最后，包含最有一位
'''

'''
#增删改查
names = ["ZhangYang","GunYun","XiangPeng","XuLiangchen"]
names.append("LeiHaidong")         #.append 最后一位
names.insert(1,"ChenRonghua")         # 将ChenRonghua 插入到第1位， 原第一位的数据会向后移一位
names[2] = "XieDi"              #修改，将第二位改为“XieDi

#Delete
#names.remove("ChenRonghua")        #.remove 删除，直接删数据
#del names[1]              #指定下标删除
names.pop(1)              #.pop 删除，不输入下标 默认删最后一位
print(names)

#查找数据的下标
print(names.index("XieDi"))   #.index()  返回下标

print(names[names.index("XieDi")],names[2])        #根据下标打印数据

names = ["ZhangYang","GunYun","XiangPeng","XuLiangchen","XieDi"]
names.insert(1,"XieDi")
#print(names.count("XieDi"))
print(names)
names.reverse()
names.sort()
print(names)

names2 = [1,2,3,4]
names.extend(names2)
del names2
print(names)
'''

import copy
names = ["ZhangYang",[1,2,3,4],"GunYun","XiangPeng","XuLiangchen","XieDi"]
names2 = copy.deepcopy(names)

names[1][0] = "9"
print(names)
print(names2)
