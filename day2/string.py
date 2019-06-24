# Author：Li Ang
# encoding=utf8

name = "my name is {name} , {year} old."

print(name.capitalize())
print(name.count("m"))
print(name.center(40,"~"))
print(name.endswith("alex"))
print(name[name.find("n"):name.find("e")])


print(name.format(name="alex",year="33"))

print(name.isalnum())
print('abe12dd'.isalnum())

print('abc'.isalpha())
print('12'.isdecimal())

print('123'.isdigit())

print('AC'.isidentifier())

print('         '.isspace())


print('My Name Is s'.istitle())

print('s s d a f das '.isprintable())

print('--'.join(['1','2','3']))

print('+'.join(['a','b','c','d']))

print(name.ljust(50,'*'))

print("Name".lower())    #转换为小写
print("Name".upper())    #转换为大写


print("\n   Name \n".lstrip())        #去掉最左边的回车空格
print("\n   Name   \n".rstrip())       #去掉最右边的回车空格
print("\n   Name  \n  is \n".strip())       #去掉两头的回车空格
print("-------")

p = str.maketrans("abcdef","123456")

print("af b".translate(p))

print("My Name is ali ".replace("a","X"))   #替换所有字符
print("My Name is ali ".replace("a","X",1))   #替换1个字符

print("My Name is is".rfind('i'))    #右边最后字符的下标
#      0123456789

print("My Name is".split())       #转换列表
print("My Name is".split("a"))

print("My Name is".swapcase())      #强制大小写转换
