# Author：Li Ang
# encoding=utf8


name = ["Tom","Natasha","Jerry","Nike"]
print(name[-3:-1])

name.insert(1,"test")
print(name)

for i in enumerate(name):                #enumeratr 里面的数据只有两个，下标和数据
    print(i)

choice = input(">>>:")

print(type(choice))

if choice.isdigit():                       #isdigit 判断是否为数字
    print("True")
else:
    print("Flase")


for i in range(6):
    print("******")
