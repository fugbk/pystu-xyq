# encoding = utf-8
__author__ = "Ang Li"

def __init__(self,name,sex):
    self.name = name
    self.sex = sex

Dog_class = type("Dog",(object,),{"role":"dog","age":21,"__init__":__init__})

d = Dog_class("Tom","M")

print(d.role,d.age,d.name,d.sex)


