# Author：Liang
# encoding=utf8

'''
name = input("Name:")
age = int(input("Age:"))
print(type(name),type(age))
print(name,"\n",age)
'''

'''
msg = '我是谁'
print(msg)
print(msg.encode("utf-8"))     #utf8 格式字符串 encode 编码二进制格式
print(msg.encode())    #python3 中encode 默认为utf8 格式
print(msg.encode(encoding="utf-8").decode(encoding="utf-8"))  #decode 解码为utf8 格式的字符串

produce_list = [
    ('iphone',8000),
    ('book',4000),
    ('mac',18000),
    ('watch',3000)
]

choice = input("Your choice: ")
print(choice)
choice_pice = int(produce_list[choice][1])

print(choice_pice)
'''


info = {
    "zhangshan","234"
    "lishi","2355"
}

info.pop("lishi")