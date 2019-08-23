# encoding = utf-8
__author__ = "Ang Li"

class Person(object):
    def __init__(self,name,age):
        self.sex = "M"
        self.name = name
        self.age = age

    def talk(self):
        print(self.name, "is not speaking...")

p = Person("Tom",22)

# mod = sys.modules[__name__]
#
# if hasattr(mod,"p"):
#     func = getattr(mod,"p")
#     print(func)

# def talk(self):
#     print(self.name,"is speaking...")
#

#
# # 判断属性
# if hasattr(p,"name"):
#     print("L-------------")
# # 获取属性,执行方法
# user_cmd = input(">>> ").strip()
# # if hasattr(p,user_cmd): # 可以先判断有没有这个属性, 然后打印这个属性的值
# #     value = getattr(p,user_cmd)
# #     print(value)
# if hasattr(p,user_cmd):
#     func = getattr(p,user_cmd)
#     func()
#
# # 修改属性, 赋值
# setattr(p,"sex","Female") # 定义一个新属性
# print(p.sex)
#
# setattr(p,"age",20) # 修改原有的属性
# print(p.age)
# p.talk()
# setattr(p,"talk",talk)
# p.talk(p)


# # 删除属性
# delattr(p,"age")
# print(p.age)